import streamlit as st
import random
import importlib
import urllib.parse
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION DES TRAITS ---
TRAITS_DISPO = [
    "pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", 
    "audacieux", "soumis", "dominant", "souple", "sportif", 
    "timide", "coquin", "voyeur", "romantiaue", "esclave", 
    "gourmand", "intello", "sournois", "menteur"
]

CONTRADICTIONS = {
    "soumis": "dominant", "dominant": "soumis",
    "timide": "provocateur", "provocateur": "timide",
    "esclave": "dominant", "menteur": "romantiaue"
}

st.set_page_config(page_title="Générateur X", layout="centered")

# --- CONNEXION GOOGLE SHEETS ---
try:
    # Connexion utilisant l'URL définie dans les Secrets Streamlit
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception:
    st.error("⚠️ Erreur de connexion au Sheets. Vérifie tes 'Secrets' sur Streamlit.")

# --- INITIALISATION DES VARIABLES ---
if 'ready' not in st.session_state:
    st.session_state.ready = False
if 'j1_defi' not in st.session_state:
    st.session_state.j1_defi = None
if 'j2_defi' not in st.session_state:
    st.session_state.j2_defi = None

# --- FONCTIONS LOGIQUES ---

def obtenir_tous_les_defis(trait_nom):
    """Récupère les défis locaux (.py) et ceux du Sheets filtrés par trait"""
    defis_totaux = []
    
    # 1. Lecture des fichiers locaux (.py)
    try:
        mod = importlib.import_module(trait_nom)
        defis_totaux.extend(mod.get_defis('Mixte'))
    except:
        pass
    
    # 2. Lecture du Google Sheets (Filtre sur la colonne 'Trait')
    try:
        df = conn.read(ttl=0) # ttl=0 pour forcer la lecture des nouveaux ajouts
        # Filtrage : On compare le trait demandé avec la colonne 'Trait' du Sheets
        defis_extra = df[df['Trait'].str.lower() == trait_nom.lower()]['Défi'].tolist()
        defis_totaux.extend(defis_extra)
    except:
        pass
        
    return defis_totaux

def enregistrer_nouveau_defi(trait, texte, auteur):
    """Ajoute une ligne dans le Google Sheets avec Trait, Défi et Auteur"""
    try:
        df_actuel = conn.read(ttl=0)
        nouveau_row = pd.DataFrame([{"Trait": trait, "Défi": texte, "Auteur": auteur}])
        df_final = pd.concat([df_actuel, nouveau_row], ignore_index=True)
        conn.update(data=df_final)
        st.success(f"✅ Défi enregistré par {auteur} !")
    except Exception as e:
        st.error(f"Erreur d'enregistrement : {e}")

def generer_tour_j1():
    t = random.choice(st.session_state.traits_pour_j1)
    liste = obtenir_tous_les_defis(t)
    st.session_state.j1_trait = t
    st.session_state.j1_defi = random.choice(liste) if liste else "Aucun défi trouvé."

def generer_tour_j2():
    t = random.choice(st.session_state.traits_pour_j2)
    liste = obtenir_tous_les_defis(t)
    st.session_state.j2_trait = t
    st.session_state.j2_defi = random.choice(liste) if liste else "Aucun défi trouvé."

# --- INTERFACE UTILISATEUR ---

query_params = st.query_params

# CAS A : ÉCRAN PARTENAIRE (Lien reçu)
if "j2_nom" in query_params:
    st.title(f"🔥 Session de {query_params['j2_nom']}")
    st.write(f"Ton partenaire **{query_params['j1_nom']}** t'attend.")
    
    st.subheader(f"Décris {query_params['j1_nom']}")
    traits_j1 = st.multiselect("Choisis jusqu'à 5 traits :", TRAITS_DISPO, max_selections=5)
    
    if st.button("Lancer le jeu !"):
        if traits_j1:
            st.session_state.ready = True
            st.session_state.traits_pour_j1 = traits_j1
            st.session_state.traits_pour_j2 = query_params.get_all("j2_traits")
            st.session_state.j1_nom = query_params['j1_nom']
            st.session_state.j2_nom = query_params['j2_nom']
            generer_tour_j1()
            generer_tour_j2()
            st.rerun()

# CAS B : ÉCRAN CRÉATEUR (Initialisation)
else:
    st.title("🔥 Configuration du jeu")
    c1, c2 = st.columns(2)
    with c1:
        j1_n = st.text_input("Ton Prénom (Joueur A)")
    with c2:
        j2_n = st.text_input("Prénom du Partenaire (Joueur B)")
    
    st.divider()
    traits_j2 = st.multiselect(f"Décris {j2_n} :", TRAITS_DISPO)
    
    # Vérification des contradictions
    conflits = [t for t in traits_j2 if t in CONTRADICTIONS and CONTRADICTIONS[t] in traits_j2]
    if conflits:
        st.error(f"⚠️ Contradiction : Tu ne peux pas être '{conflits[0]}' et '{CONTRADICTIONS[conflits[0]]}' !")

    if st.button("Créer le lien de partage"):
        if j1_n and j2_n and traits_j2 and not conflits:
            base_url = "https://generateur-x-live.streamlit.app/" # Remplace par ton URL réelle
            params = {"j1_nom": j1_n, "j2_nom": j2_n, "j2_traits": traits_j2}
            url_finale = f"{base_url}?{urllib.parse.urlencode(params, doseq=True)}"
            st.success("Lien prêt ! Envoie-le à ton partenaire :")
            st.code(url_finale)

# --- ZONE DE JEU ACTIVE ---
if st.session_state.ready:
    st.divider()
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader(f"📍 {st.session_state.j1_nom}")
        st.info(f"**TRAIT : {st.session_state.j1_trait.upper()}**\n\n{st.session_state.j1_defi}")
        if st.button(f"🔄 {st.session_state.j2_nom} change ce défi"):
            generer_tour_j1()
            st.rerun()

    with col_b:
        st.subheader(f"📍 {st.session_state.j2_nom}")
        st.warning(f"**TRAIT : {st.session_state.j2_trait.upper()}**\n\n{st.session_state.j2_defi}")
        if st.button(f"🔄 {st.session_state.j1_nom} change ce défi"):
            generer_tour_j2()
            st.rerun()

    # SECTION AJOUT DE DÉFI
    st.divider()
    with st.expander("🆕 Proposer un défi permanent"):
        qui_ecrit = st.radio("Qui écrit ?", [st.session_state.j1_nom, st.session_state.j2_nom])
        t_save = st.selectbox("Pour quel trait ?", TRAITS_DISPO)
        txt_save = st.text_area("Texte du défi :")
        if st.button("Enregistrer dans la base"):
            if txt_save:
                enregistrer_nouveau_defi(t_save, txt_save, qui_ecrit)
            else:
                st.warning("Le texte est vide !")

    # SECTION HISTORIQUE
    st.subheader("🌍 Derniers défis de la communauté")
    try:
        df_h = conn.read(ttl=0)
        if not df_h.empty:
            st.table(df_h.tail(5)[['Trait', 'Défi', 'Auteur']])
    except:
        st.write("Historique indisponible.")
