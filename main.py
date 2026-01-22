import streamlit as st
import random, urllib.parse, pandas as pd, time, firebase_admin
from firebase_admin import credentials, firestore
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION ---
TRAITS_DISPO = ["pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", "audacieux", "soumis", "dominant", "souple", "sportif", "timide", "coquin", "voyeur", "romantiaue", "esclave", "gourmand", "intello", "sournois", "menteur"]

st.set_page_config(page_title="Live stream ", page_icon="🔥", layout="wide")

# --- AUDIO & STYLE ---
SOUND_NOTIF = "https://www.soundjay.com/buttons/sounds/button-3.mp3"
SOUND_MODIF = "https://www.soundjay.com/buttons/sounds/beep-07a.mp3"
SOUND_VALID = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"

st.markdown(f"""
    <style>
    div.stButton > button:first-child {{ background-color: #28a745; color: white; border-radius: 12px; height: 3.5em; width: 100%; font-weight: bold; border: none; font-size: 18px; }}
    .score-box {{ font-size: 22px; font-weight: bold; text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 15px; border: 1px solid #ddd; }}
    .status-wait {{ background-color: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 1px solid #ffeeba; }}
    .alert-modif {{ background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; margin-bottom: 10px; border: 1px solid #f5c6cb; }}
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

def obtenir_un_defi(trait, genre):
    try:
        df = conn_sheets.read(worksheet="Sheet1", ttl=5)
        mask = (df['Trait'].str.lower() == trait.lower()) & (df['Genre'].isin([genre, "Tous"]))
        return random.choice(df[mask]['Défi'].tolist())
    except: return "Fais un bisou à ton partenaire"

# --- LOGIQUE D'ÉTAT ---
doc = state_ref.get()
state = doc.to_dict() if doc.exists else None
params = st.query_params
role = params.get("role")

# ETAPE 0 : SETUP JOUEUR A
if not state:
    st.title("🔥 Divine Pulse - Création")
    n1 = st.text_input("Ton Prénom (A)")
    s1 = st.radio("Ton Sexe", ["Homme", "Femme"], horizontal=True, key="s1")
    pw1 = st.text_input("Ton Mot de Passe", type="password")
    n2 = st.text_input("Prénom de ton partenaire (B)")
    traits_b = st.multiselect(f"Décris la personnalité de {n2} :", TRAITS_DISPO)
    
    if st.button("🚀 Générer l'invitation"):
        if n1 and pw1 and n2 and traits_b:
            state_ref.set({
                "n1": n1, "s1": s1, "pw1": pw1, "traits_de_b": traits_b, "n2": n2,
                "step": 1, "update_ts": time.time(), "last_action": "init"
            })
            st.success("Session prête ! Envoie ce lien à B :")
            st.code(f"https://generateur-x-live.streamlit.app/?role=B")
            time.sleep(2); st.rerun()

# ETAPE 1 : SETUP JOUEUR B
elif state.get("step") == 1:
    if role == "B":
        st.title(f"💋 Bienvenue {state.get('n2')}")
        s2 = st.radio("Ton Sexe", ["Homme", "Femme"], horizontal=True, key="s2")
        pw2 = st.text_input("Choisis ton Mot de Passe", type="password")
        traits_a = st.multiselect(f"Décris la personnalité de {state.get('n1')} :", TRAITS_DISPO)
        
        if st.button("🔥 Lancer le Jeu"):
            if pw2 and traits_a:
                genre = "H/H" if state['s1']=="Homme" and s2=="Homme" else "F/F" if state['s1']=="Femme" and s2=="Femme" else "Mixte"
                t_a, t_b = random.choice(traits_a), random.choice(state['traits_de_b'])
                state_ref.update({
                    "s2": s2, "pw2": pw2, "traits_de_a": traits_a, "genre": genre,
                    "J1_Trait": t_b, "J1_Defi": obtenir_un_defi(t_b, genre), "J1_Score": 0, "J1_Ready": False,
                    "J2_Trait": t_a, "J2_Defi": obtenir_un_defi(t_a, genre), "J2_Score": 0, "J2_Ready": False,
                    "step": 2, "update_ts": time.time(), "last_action": "start"
                })
                st.rerun()
    else:
        st.info(f"⏳ En attente de {state.get('n2')}..."); time.sleep(4); st.rerun()

# ETAPE 2 : LE JEU (GESTION DU TOUR PAR TOUR)
else:
    if f"auth_{role}" not in st.session_state:
        st.title("🔒 Accès sécurisé")
        upw = st.text_input("Password :", type="password")
        if st.button("Se connecter"):
            correct = state.get('pw1') if role == 'A' else state.get('pw2')
            if upw == correct: st.session_state[f"auth_{role}"] = True; st.rerun()
        st.stop()

    # --- LOGIQUE DE PASSAGE AU TOUR SUIVANT (Les 2 validés) ---
    if state.get("J1_Ready") and state.get("J2_Ready"):
        genre = state['genre']
        nt_a, nt_b = random.choice(state['traits_de_a']), random.choice(state['traits_de_b'])
        state_ref.update({
            "J1_Trait": nt_b, "J1_Defi": obtenir_un_defi(nt_b, genre), "J1_Score": state['J1_Score']+1, "J1_Ready": False,
            "J2_Trait": nt_a, "J2_Defi": obtenir_un_defi(nt_a, genre), "J2_Score": state['J2_Score']+1, "J2_Ready": False,
            "update_ts": time.time(), "last_action": "new_round"
        })
        st.rerun()

    # --- SYNC AUDIO ---
    if "last_ts" not in st.session_state: st.session_state.last_ts = state['update_ts']
    if state['update_ts'] > st.session_state.last_ts:
        st.session_state.last_ts = state['update_ts']
        if "jv" not in st.session_state:
            snd = "modif-sound" if state.get("last_action") == "modif" else "notif-sound"
            st.markdown(f'<script>document.getElementById("{snd}").play();</script>', unsafe_allow_html=True)
        else: del st.session_state["jv"]

    st.title(f"🎮 {state['n1']} & {state['n2']}")
    if state.get("last_action") == "modif":
        st.markdown('<div class="alert-modif">⚠️ Défi modifié manuellement par le partenaire !</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    
    # AFFICHAGE JOUEUR 1 (A)
    with c1:
        st.markdown(f"<div class='score-box'>Score {state['n1']} : {state['J1_Score']}</div>", unsafe_allow_html=True)
        st.info(f"**DÉFI POUR {state['n1']} :**\n\n{state['J1_Defi']}")
        if state.get("J1_Ready"): st.success("✅ Validé ! En attente de l'autre...")
        elif role == "B":
            if st.button(f"Valider l'action de {state['n1']}"):
                st.session_state["jv"] = True; st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                state_ref.update({"J1_Ready": True, "update_ts": time.time(), "last_action": "valid"})
                st.rerun()
            with st.expander("✏️ Modifier"):
                n_txt = st.text_area("Nouveau texte pour A :", key="ma")
                if st.button("Envoyer Modif A"):
                    state_ref.update({"J1_Defi": n_txt, "update_ts": time.time(), "last_action": "modif"}); st.rerun()

    # AFFICHAGE JOUEUR 2 (B)
    with c2:
        st.markdown(f"<div class='score-box'>Score {state['n2']} : {state['J2_Score']}</div>", unsafe_allow_html=True)
        st.warning(f"**DÉFI POUR {state['n2']} :**\n\n{state['J2_Defi']}")
        if state.get("J2_Ready"): st.success("✅ Validé ! En attente de l'autre...")
        elif role == "A":
            if st.button(f"Valider l'action de {state['n2']}"):
                st.session_state["jv"] = True; st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                state_ref.update({"J2_Ready": True, "update_ts": time.time(), "last_action": "valid"})
                st.rerun()
            with st.expander("✏️ Modifier"):
                n_txt = st.text_area("Nouveau texte pour B :", key="mb")
                if st.button("Envoyer Modif B"):
                    state_ref.update({"J2_Defi": n_txt, "update_ts": time.time(), "last_action": "modif"}); st.rerun()

    if role == "A" and st.sidebar.button("♻️ Reset"):
        state_ref.delete(); st.rerun()

    time.sleep(4); st.rerun()
