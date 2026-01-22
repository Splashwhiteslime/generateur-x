import streamlit as st
import random
import urllib.parse
import pandas as pd
import time
import requests
import firebase_admin
from firebase_admin import credentials, firestore
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION ---
TRAITS_DISPO = ["pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", "audacieux", "soumis", "dominant", "souple", "sportif", "timide", "coquin", "voyeur", "romantiaue", "esclave", "gourmand", "intello", "sournois", "menteur"]

st.set_page_config(page_title="Générateur X Live", layout="wide")

# --- CONNEXIONS ---
# 1. Google Sheets (Lecture des défis existants)
conn_sheets = st.connection("gsheets", type=GSheetsConnection)

# 2. Firebase (Synchronisation et nouveaux défis)
if not firebase_admin._apps:
    try:
        fb_dict = dict(st.secrets["firebase"])
        cred = credentials.Certificate(fb_dict)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error("Erreur de connexion Firebase. Vérifie tes Secrets.")

db = firestore.client()

# --- FONCTIONS TECHNIQUES ---

def reduire_url(url_longue):
    """Raccourcit l'URL via TinyURL"""
    try:
        api_url = f"http://tinyurl.com/api-create.php?url={urllib.parse.quote(url_longue)}"
        return requests.get(api_url, timeout=5).text
    except:
        return url_longue

def push_state(j1_t, j1_d, j2_t, j2_d):
    """Met à jour la session live dans Firebase"""
    db.collection("sessions").document("LIVE").set({
        "J1_Trait": j1_t, "J1_Defi": j1_d,
        "J2_Trait": j2_t, "J2_Defi": j2_d,
        "timestamp": time.time()
    })

def pull_state():
    """Lit l'état actuel de la session"""
    doc = db.collection("sessions").document("LIVE").get()
    return doc.to_dict() if doc.exists else None

def ajouter_nouveau_defi_firebase(trait, texte, auteur, genre):
    """Enregistre un nouveau défi dans Firestore"""
    db.collection("nouveaux_defis").add({
        "Trait": trait.lower(),
        "Défi": texte,
        "Auteur": auteur,
        "Genre": genre,
        "Date": time.time()
    })

def obtenir_defis_combines(trait_nom, genre_session):
    """Récupère Sheets + Firebase"""
    liste_defis = []
    
    # Lecture Sheets
    try:
        df_s = conn_sheets.read(worksheet="Sheet1", ttl=10)
        mask = (df_s['Trait'].str.lower() == trait_nom.lower()) & (df_s['Genre'].isin([genre_session, "Tous"]))
        liste_defis = df_s[mask]['Défi'].tolist()
    except: pass
    
    # Lecture Firebase
    try:
        fb_docs = db.collection("nouveaux_defis").where("Trait", "==", trait_nom.lower()).stream()
        for doc in fb_docs:
            d = doc.to_dict()
            if d.get("Genre") in [genre_session, "Tous"]:
                liste_defis.append(d["Défi"])
    except: pass
        
    return liste_defis if liste_defis else ["Fais un bisou (Défaut)"]

# --- GESTION DES RÔLES ET URL ---
query_params = st.query_params
role = query_params.get("role", "A")
genre_actuel = query_params.get("genre", "Mixte")

# --- ETAPE 1 : SETUP ---
if "ready_check" not in query_params and "j2_nom" not in query_params:
    st.title("🔥 Setup Session Live")
    
    col1, col2 = st.columns(2)
    with col1:
        j1 = st.text_input("Ton Prénom (A)")
        sexe_a = st.radio(f"Sexe de A", ["Homme", "Femme"], horizontal=True)
    with col2:
        j2 = st.text_input("Prénom Partenaire (B)")
        sexe_b = st.radio(f"Sexe de B", ["Homme", "Femme"], horizontal=True)
    
    # Déduction auto du genre
    genre_auto = "H/H" if sexe_a=="Homme" and sexe_b=="Homme" else "F/F" if sexe_a=="Femme" and sexe_b=="Femme" else "Mixte"
    st.info(f"Type détecté : **{genre_auto}**")
    
    t_j2 = st.multiselect(f"Sélectionne les traits de {j2} :", TRAITS_DISPO)
    
    if st.button("🚀 Créer la session"):
        # Tirage initial
        t1 = random.choice(TRAITS_DISPO)
        d1 = random.choice(obtenir_defis_combines(t1, genre_auto))
        t2 = random.choice(t_j2) if t_j2 else random.choice(TRAITS_DISPO)
        d2 = random.choice(obtenir_defis_combines(t2, genre_auto))
        
        push_state(t1, d1, t2, d2)
        
        base_url = "https://generateur-x-live.streamlit.app/"
        p = {"j1_nom": j1, "j2_nom": j2, "ready_check": "yes", "j2_traits": t_j2, "genre": genre_auto}
        
        with st.spinner("Raccourcissement des liens..."):
            url_a = reduire_url(f"{base_url}?{urllib.parse.urlencode({**p, 'role': 'A'})}")
            url_b = reduire_url(f"{base_url}?{urllib.parse.urlencode({**p, 'role': 'B'})}")
        
        st.success("Session configurée !")
        st.write(f"📱 **Lien pour TOI (A) :** `{url_a}`")
        st.write(f"🎁 **Lien pour PARTENAIRE (B) :** `{url_b}`")

# --- ETAPE 2 : ZONE DE JEU ---
else:
    state = pull_state()
    if state:
        st.title(f"💋 {genre_actuel} : {query_params.get('j1_nom')} & {query_params.get('j2_nom')}")
        st.write(f"Connecté en tant que : **Joueur {role}**")
        
        col_a, col_b = st.columns(2)

        # COLONNE JOUEUR A
        with col_a:
            st.header(query_params.get('j1_nom'))
            st.info(f"**{state['J1_Trait'].upper()}**\n\n{state['J1_Defi']}")
            if role == "B":
                if st.button(f"✅ Valider défi de {query_params.get('j1_nom')}"):
                    new_t = random.choice(TRAITS_DISPO)
                    push_state(new_t, random.choice(obtenir_defis_combines(new_t, genre_actuel)), state['J2_Trait'], state['J2_Defi'])
                    st.rerun()
                with st.expander("🛠 Proposer un autre défi"):
                    txt = st.text_area("Nouveau texte :", key="mod_a")
                    if st.button("Enregistrer"):
                        ajouter_nouveau_defi_firebase(state['J1_Trait'], txt, query_params.get('j2_nom'), genre_actuel)
                        push_state(state['J1_Trait'], txt, state['J2_Trait'], state['J2_Defi'])
                        st.rerun()

        # COLONNE JOUEUR B
        with col_b:
            st.header(query_params.get('j2_nom'))
            st.warning(f"**{state['J2_Trait'].upper()}**\n\n{state['J2_Defi']}")
            if role == "A":
                if st.button(f"✅ Valider défi de {query_params.get('j2_nom')}"):
                    ts_b = query_params.get_all("j2_traits")
                    new_t = random.choice(ts_b) if ts_b else random.choice(TRAITS_DISPO)
                    push_state(state['J1_Trait'], state['J1_Defi'], new_t, random.choice(obtenir_defis_combines(new_t, genre_actuel)))
                    st.rerun()
                with st.expander("🛠 Proposer un autre défi"):
                    txt = st.text_area("Nouveau texte :", key="mod_b")
                    if st.button("Enregistrer"):
                        ajouter_nouveau_defi_firebase(state['J2_Trait'], txt, query_params.get('j1_nom'), genre_actuel)
                        push_state(state['J1_Trait'], state['J1_Defi'], state['J2_Trait'], txt)
                        st.rerun()

        # Rafraîchissement automatique pour voir les actions de l'autre
        time.sleep(4)
        st.rerun()
