import streamlit as st
import random
import urllib.parse
import pandas as pd
import time
import requests
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION ---
TRAITS_DISPO = ["pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", "audacieux", "soumis", "dominant", "souple", "sportif", "timide", "coquin", "voyeur", "romantiaue", "esclave", "gourmand", "intello", "sournois", "menteur"]

st.set_page_config(page_title="Générateur X Live", layout="wide")
conn = st.connection("gsheets", type=GSheetsConnection)

# --- FONCTIONS TECHNIQUES ---
def reduire_url(url_longue):
    try:
        api_url = f"http://tinyurl.com/api-create.php?url={urllib.parse.quote(url_longue)}"
        return requests.get(api_url, timeout=5).text
    except: return url_longue

def push_state(j1_t, j1_d, j2_t, j2_d):
    df_sync = pd.DataFrame([{"ID": "LIVE", "J1_Trait": j1_t, "J1_Defi": j1_d, "J2_Trait": j2_t, "J2_Defi": j2_d}])
    conn.update(worksheet="Session", data=df_sync)

def pull_state():
    try:
        df = conn.read(worksheet="Session", ttl=0)
        return df.iloc[0]
    except: return None

def obtenir_defis(trait_nom, genre_session):
    try:
        df = conn.read(worksheet="Sheet1", ttl=10) 
        mask = (df['Trait'].str.lower() == trait_nom.lower()) & \
               (df['Genre'].isin([genre_session, "Tous"]))
        res = df[mask]['Défi'].tolist()
        return res if res else [f"Défi par défaut ({genre_session})"]
    except: return ["Fais un bisou"]

def ajouter_nouveau_defi_base(trait, texte, auteur, genre):
    try:
        df_actuel = conn.read(worksheet="Sheet1", ttl=0)
        nouveau_row = pd.DataFrame([{"Trait": trait, "Défi": texte, "Auteur": auteur, "Genre": genre}])
        df_final = pd.concat([df_actuel, nouveau_row], ignore_index=True)
        conn.update(worksheet="Sheet1", data=df_final)
        return True
    except: return False

# --- LOGIQUE URL & RÔLES ---
query_params = st.query_params
role = query_params.get("role", "A")
genre_actuel = query_params.get("genre", "Mixte")

# --- ETAPE 1 : SETUP (DÉDUCTION AUTOMATIQUE DU GENRE) ---
if "ready_check" not in query_params and "j2_nom" not in query_params:
    st.title("🔥 Setup Session Live")
    
    col1, col2 = st.columns(2)
    with col1:
        j1 = st.text_input("Prénom Joueur A")
        sexe_a = st.radio(f"Sexe de {j1 if j1 else 'A'}", ["Homme", "Femme"], horizontal=True)
    with col2:
        j2 = st.text_input("Prénom Joueur B")
        sexe_b = st.radio(f"Sexe de {j2 if j2 else 'B'}", ["Homme", "Femme"], horizontal=True)
    
    # DÉDUCTION AUTOMATIQUE
    if sexe_a == "Homme" and sexe_b == "Homme": genre_auto = "H/H"
    elif sexe_a == "Femme" and sexe_b == "Femme": genre_auto = "F/F"
    else: genre_auto = "Mixte"
    
    st.info(f"💡 Type de rencontre détecté : **{genre_auto}**")
    
    t_j2 = st.multiselect(f"Traits de {j2} :", TRAITS_DISPO)
    
    if st.button("🚀 Créer la session"):
        t1 = random.choice(TRAITS_DISPO)
        d1 = random.choice(obtenir_defis(t1, genre_auto))
        t2 = random.choice(t_j2) if t_j2 else random.choice(TRAITS_DISPO)
        d2 = random.choice(obtenir_defis(t2, genre_auto))
        
        push_state(t1, d1, t2, d2)
        
        base_url = "https://generateur-x-live.streamlit.app/"
        p = {"j1_nom": j1, "j2_nom": j2, "ready_check": "yes", "j2_traits": t_j2, "genre": genre_auto}
        
        url_a = reduire_url(f"{base_url}?{urllib.parse.urlencode({**p, 'role': 'A'})}")
        url_b = reduire_url(f"{base_url}?{urllib.parse.urlencode({**p, 'role': 'B'})}")
        
        st.success("Session configurée !")
        st.write(f"📱 **Ton lien (A) :** `{url_a}`")
        st.write(f"🎁 **Lien Partenaire (B) :** `{url_b}`")

# --- ETAPE 2 : ZONE DE JEU ---
else:
    state = pull_state()
    if state is not None:
        st.title(f"💋 {genre_actuel} : {query_params.get('j1_nom')} & {query_params.get('j2_nom')}")
        col_a, col_b = st.columns(2)

        # JOUEUR A
        with col_a:
            st.header(query_params.get('j1_nom'))
            st.info(f"**{state['J1_Trait'].upper()}**\n\n{state['J1_Defi']}")
            if role == "B":
                if st.button(f"✅ Valider {query_params.get('j1_nom')}"):
                    new_t = random.choice(TRAITS_DISPO)
                    push_state(new_t, random.choice(obtenir_defis(new_t, genre_actuel)), state['J2_Trait'], state['J2_Defi'])
                    st.rerun()
                with st.expander("🛠 Modifier"):
                    txt = st.text_area("Nouveau texte :", value=state['J1_Defi'], key="m1")
                    if st.button("Enregistrer"):
                        ajouter_nouveau_defi_base(state['J1_Trait'], txt, query_params.get('j2_nom'), genre_actuel)
                        push_state(state['J1_Trait'], txt, state['J2_Trait'], state['J2_Defi'])
                        st.rerun()

        # JOUEUR B
        with col_b:
            st.header(query_params.get('j2_nom'))
            st.warning(f"**{state['J2_Trait'].upper()}**\n\n{state['J2_Defi']}")
            if role == "A":
                if st.button(f"✅ Valider {query_params.get('j2_nom')}"):
                    ts_b = query_params.get_all("j2_traits")
                    new_t = random.choice(ts_b) if ts_b else random.choice(TRAITS_DISPO)
                    push_state(state['J1_Trait'], state['J1_Defi'], new_t, random.choice(obtenir_defis(new_t, genre_actuel)))
                    st.rerun()
                with st.expander("🛠 Modifier"):
                    txt = st.text_area("Nouveau texte :", value=state['J2_Defi'], key="m2")
                    if st.button("Enregistrer"):
                        ajouter_nouveau_defi_base(state['J2_Trait'], txt, query_params.get('j1_nom'), genre_actuel)
                        push_state(state['J1_Trait'], state['J1_Defi'], state['J2_Trait'], txt)
                        st.rerun()

        time.sleep(4)
        st.rerun()
