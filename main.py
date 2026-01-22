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

# --- FONCTIONS ---
def reduire_url(url_longue):
    try:
        api_url = f"http://tinyurl.com/api-create.php?url={urllib.parse.quote(url_longue)}"
        return requests.get(api_url, timeout=5).text
    except:
        return url_longue

def push_state(j1_t, j1_d, j2_t, j2_d):
    df_sync = pd.DataFrame([{"ID": "LIVE", "J1_Trait": j1_t, "J1_Defi": j1_d, "J2_Trait": j2_t, "J2_Defi": j2_d}])
    conn.update(worksheet="Session", data=df_sync)

def pull_state():
    try:
        df = conn.read(worksheet="Session", ttl=0)
        return df.iloc[0]
    except:
        return None

def obtenir_defis(trait_nom, genre_session):
    """Filtre par trait ET par genre (ex: Mixte, H/H, F/F)"""
    try:
        df = conn.read(worksheet="Sheet1", ttl=10) 
        # On garde les défis du trait qui correspondent au genre choisi OU marqués 'Tous'
        mask = (df['Trait'].str.lower() == trait_nom.lower()) & \
               (df['Genre'].isin([genre_session, "Tous"]))
        res = df[mask]['Défi'].tolist()
        return res if res else [f"Fais un bisou ({genre_session})"]
    except:
        return ["Fais un bisou"]

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

# --- ETAPE 1 : SETUP ---
if "ready_check" not in query_params and "j2_nom" not in query_params:
    st.title("🔥 Configuration Session Live")
    
    col_inf1, col_inf2, col_inf3 = st.columns(3)
    with col_inf1: j1 = st.text_input("Prénom A")
    with col_inf2: j2 = st.text_input("Prénom B")
    with col_inf3: genre_sel = st.selectbox("Type de rencontre", ["Mixte", "H/H", "F/F"])
    
    t_j2 = st.multiselect(f"Traits de {j2} :", TRAITS_DISPO)
    
    if st.button("🚀 Créer la session"):
        # Tirage initial selon le genre
        t1 = random.choice(TRAITS_DISPO)
        d1 = random.choice(obtenir_defis(t1, genre_sel))
        t2 = random.choice(t_j2) if t_j2 else random.choice(TRAITS_DISPO)
        d2 = random.choice(obtenir_defis(t2, genre_sel))
        
        push_state(t1, d1, t2, d2)
        
        base_url = "https://generateur-x-live.streamlit.app/"
        p = {"j1_nom": j1, "j2_nom": j2, "ready_check": "yes", "j2_traits": t_j2, "genre": genre_sel}
        
        url_a = reduire_url(f"{base_url}?{urllib.parse.urlencode({**p, 'role': 'A'})}")
        url_b = reduire_url(f"{base_url}?{urllib.parse.urlencode({**p, 'role': 'B'})}")
        
        st.success("Session prête !")
        st.write(f"📱 **Lien A :** `{url_a}`")
        st.write(f"🎁 **Lien B :** `{url_b}`")

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
