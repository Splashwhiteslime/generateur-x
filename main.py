import streamlit as st
import random, urllib.parse, pandas as pd, time, firebase_admin
from firebase_admin import credentials, firestore
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION ---
TRAITS_DISPO = ["pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", "audacieux", "soumis", "dominant", "souple", "sportif", "timide", "coquin", "voyeur", "romantiaue", "esclave", "gourmand", "intello", "sournois", "menteur"]

st.set_page_config(page_title="Divine Pulse", page_icon="🔥", layout="wide")

# --- AUDIO & STYLE ---
SOUND_NOTIF = "https://www.soundjay.com/buttons/sounds/button-3.mp3"
SOUND_MODIF = "https://www.soundjay.com/buttons/sounds/beep-07a.mp3" # Son différent pour modif
SOUND_VALID = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"

st.markdown(f"""
    <style>
    div.stButton > button:first-child {{ background-color: #28a745; color: white; border-radius: 12px; height: 3.5em; width: 100%; font-weight: bold; border: none; }}
    .score-box {{ font-size: 22px; font-weight: bold; text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 15px; border: 1px solid #ddd; }}
    .alert-modif {{ background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; border: 1px solid #ffeeba; text-align: center; font-weight: bold; margin-bottom: 10px; animation: blinker 1.5s linear infinite; }}
    @keyframes blinker {{ 50% {{ opacity: 0.5; }} }}
    </style>
    <audio id="notif-sound" src="{SOUND_NOTIF}" preload="auto"></audio>
    <audio id="modif-sound" src="{SOUND_MODIF}" preload="auto"></audio>
    <audio id="valid-sound" src="{SOUND_VALID}" preload="auto"></audio>
""", unsafe_allow_html=True)

# --- CONNEXIONS ---
conn_sheets = st.connection("gsheets", type=GSheetsConnection)
if not firebase_admin._apps:
    fb_dict = dict(st.secrets["firebase"])
    cred = credentials.Certificate(fb_dict)
    firebase_admin.initialize_app(cred)
db = firestore.client()
state_ref = db.collection("sessions").document("LIVE")

# --- FONCTIONS ---
def obtenir_un_defi(trait, genre):
    try:
        df = conn_sheets.read(worksheet="Sheet1", ttl=5)
        mask = (df['Trait'].str.lower() == trait.lower()) & (df['Genre'].isin([genre, "Tous"]))
        return random.choice(df[mask]['Défi'].tolist())
    except: return "Fais un bisou à ton partenaire"

# --- LOGIQUE ---
state = state_ref.get().to_dict() if state_ref.get().exists else None
params = st.query_params

# ÉTAPES D'INITIALISATION (A puis B)
if not state:
    # ... (Code de création par A identique au précédent)
    st.title("🔥 Divine Pulse - Setup A")
    n1 = st.text_input("Ton Prénom (A)")
    s1 = st.radio("Ton Sexe", ["Homme", "Femme"], horizontal=True)
    pw1 = st.text_input("Ton Mot de Passe", type="password")
    n2 = st.text_input("Prénom de B")
    traits_b = st.multiselect(f"Personnalité de {n2} :", TRAITS_DISPO)
    if st.button("🚀 Créer l'invitation"):
        if n1 and pw1 and n2 and traits_b:
            state_ref.set({"n1": n1, "s1": s1, "pw1": pw1, "traits_de_b": traits_b, "n2": n2, "step": 1, "update_ts": time.time(), "last_action": "init"})
            st.success("Lien pour B : https://generateur-x-live.streamlit.app/?role=B")
            time.sleep(2); st.rerun()

elif state.get("step") == 1:
    # ... (Code de finalisation par B identique au précédent)
    role = params.get("role")
    if role == "B":
        st.title(f"💋 Bienvenue {state['n2']}")
        s2 = st.radio("Ton Sexe", ["Homme", "Femme"], horizontal=True)
        pw2 = st.text_input("Ton Mot de Passe", type="password")
        traits_a = st.multiselect(f"Personnalité de {state['n1']} :", TRAITS_DISPO)
        if st.button("🔥 Lancer le Jeu"):
            genre = "H/H" if state['s1']=="Homme" and s2=="Homme" else "F/F" if state['s1']=="Femme" and s2=="Femme" else "Mixte"
            t_a, t_b = random.choice(traits_a), random.choice(state['traits_de_b'])
            state_ref.update({"s2": s2, "pw2": pw2, "traits_de_a": traits_a, "genre": genre, "J1_Trait": t_b, "J1_Defi": obtenir_un_defi(t_b, genre), "J1_Score": 0, "J2_Trait": t_a, "J2_Defi": obtenir_un_defi(t_a, genre), "J2_Score": 0, "step": 2, "update_ts": time.time(), "last_action": "start"})
            st.rerun()
    else:
        st.info(f"En attente de {state['n2']}..."); time.sleep(5); st.rerun()

# ÉTAPE 2 : LE JEU SÉCURISÉ ET SYNCHRONISÉ
else:
    role = params.get("role")
    if f"auth_{role}" not in st.session_state:
        st.title("🔒 Accès"); upw = st.text_input("Password :", type="password")
        if st.button("OK"):
            if upw == (state['pw1'] if role == 'A' else state['pw2']):
                st.session_state[f"auth_{role}"] = True; st.rerun()
        st.stop()

    # --- SYNCHRO AUDIO ET ALERTE MODIF ---
    if "last_ts" not in st.session_state: st.session_state.last_ts = state['update_ts']
    
    if state['update_ts'] > st.session_state.last_ts:
        st.session_state.last_ts = state['update_ts']
        if "jv" not in st.session_state:
            # Si c'est une modification manuelle, on joue le son de modif
            if state.get("last_action") == "modif":
                st.markdown('<script>document.getElementById("modif-sound").play();</script>', unsafe_allow_html=True)
            else:
                st.markdown('<script>document.getElementById("notif-sound").play();</script>', unsafe_allow_html=True)
        else: del st.session_state["jv"]

    st.title(f"🎮 {state['n1']} & {state['n2']}")
    
    # Message d'alerte si le défi a été modifié par le partenaire
    if state.get("last_action") == "modif":
        st.markdown('<div class="alert-modif">⚠️ Ton défi a été modifié par ton partenaire !</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"<div class='score-box'>Score {state['n1']} : {state['J1_Score']}</div>", unsafe_allow_html=True)
        st.info(f"**DÉFI DE {state['n1']} :**\n\n{state['J1_Defi']}")
        if role == "B":
            if st.button(f"✅ Valider {state['n1']}"):
                st.session_state["jv"] = True; st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                new_t = random.choice(state['traits_de_b'])
                state_ref.update({"J1_Trait": new_t, "J1_Defi": obtenir_un_defi(new_t, state['genre']), "J1_Score": state['J1_Score']+1, "update_ts": time.time(), "last_action": "valid"})
                st.rerun()
            with st.expander("✏️ Modifier son défi"):
                nouveau = st.text_area("Texte personnalisé :")
                if st.button("Envoyer modif A"):
                    state_ref.update({"J1_Defi": nouveau, "update_ts": time.time(), "last_action": "modif"})
                    st.rerun()

    with col_b:
        st.markdown(f"<div class='score-box'>Score {state['n2']} : {state['J2_Score']}</div>", unsafe_allow_html=True)
        st.warning(f"**DÉFI DE {state['n2']} :**\n\n{state['J2_Defi']}")
        if role == "A":
            if st.button(f"✅ Valider {state['n2']}"):
                st.session_state["jv"] = True; st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                new_t = random.choice(state['traits_de_a'])
                state_ref.update({"J2_Trait": new_t, "J2_Defi": obtenir_un_defi(new_t, state['genre']), "J2_Score": state['J2_Score']+1, "update_ts": time.time(), "last_action": "valid"})
                st.rerun()
            with st.expander("✏️ Modifier son défi"):
                nouveau = st.text_area("Texte personnalisé :")
                if st.button("Envoyer modif B"):
                    state_ref.update({"J2_Defi": nouveau, "update_ts": time.time(), "last_action": "modif"})
                    st.rerun()

    if role == "A" and st.sidebar.button("♻️ Reset"):
        state_ref.delete(); st.rerun()

    time.sleep(4); st.rerun()
