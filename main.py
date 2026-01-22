import streamlit as st
import random, urllib.parse, pd, time, requests, firebase_admin
from firebase_admin import credentials, firestore
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION ---
TRAITS_DISPO = ["pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", "audacieux", "soumis", "dominant", "souple", "sportif", "timide", "coquin", "voyeur", "romantiaue", "esclave", "gourmand", "intello", "sournois", "menteur"]

st.set_page_config(page_title="Générateur X Live - Full Audio", layout="wide")

# --- SYSTÈME AUDIO & CSS ---
# Notification (quand on reçoit un nouveau défi)
SOUND_NOTIF = "https://www.soundjay.com/buttons/sounds/button-3.mp3"
# Validation (quand on valide l'autre)
SOUND_VALID = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"

st.markdown(f"""
    <style>
    div.stButton > button:first-child {{
        background-color: #28a745; color: white; border-radius: 12px;
        height: 3.5em; width: 100%; font-weight: bold; font-size: 18px;
        border: none; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }}
    .score-box {{
        font-size: 22px; font-weight: bold; text-align: center;
        padding: 10px; background-color: #f0f2f6; border-radius: 10px;
        margin-bottom: 15px; border: 1px solid #ddd;
    }}
    </style>
    <audio id="notif-sound" src="{SOUND_NOTIF}" preload="auto"></audio>
    <audio id="valid-sound" src="{SOUND_VALID}" preload="auto"></audio>
""", unsafe_allow_html=True)

# --- CONNEXIONS ---
conn_sheets = st.connection("gsheets", type=GSheetsConnection)
if not firebase_admin._apps:
    fb_dict = dict(st.secrets["firebase"])
    cred = credentials.Certificate(fb_dict)
    firebase_admin.initialize_app(cred)
db = firestore.client()

# --- FONCTIONS ---
def push_state(j1_t, j1_d, j2_t, j2_d, s1, s2, pw1, pw2):
    db.collection("sessions").document("LIVE").set({
        "J1_Trait": j1_t, "J1_Defi": j1_d, "J1_Score": s1, "J1_PW": pw1,
        "J2_Trait": j2_t, "J2_Defi": j2_d, "J2_Score": s2, "J2_PW": pw2,
        "update_ts": time.time()
    })

def pull_state():
    doc = db.collection("sessions").document("LIVE").get()
    return doc.to_dict() if doc.exists else None

def obtenir_defis(trait_nom, genre_session):
    try:
        df = conn_sheets.read(worksheet="Sheet1", ttl=10)
        mask = (df['Trait'].str.lower() == trait_nom.lower()) & (df['Genre'].isin([genre_session, "Tous"]))
        res = df[mask]['Défi'].tolist()
        return res if res else ["Fais un bisou très doux"]
    except: return ["Action par défaut"]

# --- LOGIQUE DE NAVIGATION ---
params = st.query_params

if "ready" not in params:
    st.title("🔥 Setup & Audio")
    col1, col2 = st.columns(2)
    with col1:
        n1 = st.text_input("Ton Prénom (A)")
        pw1 = st.text_input("Ton MDP (A)", type="password")
        t_b = st.multiselect(f"Tempérament de B :", TRAITS_DISPO)
    with col2:
        n2 = st.text_input("Prénom Partenaire (B)")
        pw2 = st.text_input("Son MDP (B)", type="password")
        t_a = st.multiselect(f"Tes traits (A) :", TRAITS_DISPO)

    if st.button("🚀 Lancer avec Audio"):
        if t_a and t_b and pw1 and pw2:
            t1, t2 = random.choice(t_b), random.choice(t_a)
            push_state(t1, random.choice(obtenir_defis(t1, "Mixte")), t2, random.choice(obtenir_defis(t2, "Mixte")), 0, 0, pw1, pw2)
            p = {"ready": "y", "genre": "Mixte", "n1": n1, "n2": n2, "la": t_a, "lb": t_b}
            base = "https://generateur-x-live.streamlit.app/"
            url_b = f"{base}?{urllib.parse.urlencode({**p, 'role': 'B'})}"
            st.success("C'est prêt !")
            st.markdown(f"**Lien B :** `{url_b}`")
            time.sleep(5)
            st.query_params.update({**p, "role": "A"})
            st.rerun()

else:
    state = pull_state()
    role = params.get("role")
    
    if f"auth_{role}" not in st.session_state:
        st.title("🔒 Connexion")
        upw = st.text_input("Code :", type="password")
        if st.button("Entrer"):
            if upw == (state['J1_PW'] if role == 'A' else state['J2_PW']):
                st.session_state[f"auth_{role}"] = True
                st.rerun()
        st.stop()

    # --- DÉTECTION DU CHANGEMENT (Notification) ---
    if "last_ts" not in st.session_state:
        st.session_state.last_ts = state['update_ts']
    
    if state['update_ts'] > st.session_state.last_ts:
        st.session_state.last_ts = state['update_ts']
        # On ne joue le son de notif QUE si on n'est pas celui qui a validé (pour éviter le double son)
        if "just_validated" not in st.session_state:
            st.markdown('<script>document.getElementById("notif-sound").play();</script>', unsafe_allow_html=True)
        else:
            del st.session_state["just_validated"]

    # --- JEU ---
    st.title(f"🎮 {params.get('n1')} vs {params.get('n2')}")
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown(f"<div class='score-box'>Score {params.get('n1')} : {state.get('J1_Score', 0)}</div>", unsafe_allow_html=True)
        st.info(f"**CIBLE :** {state['J1_Trait'].upper()}\n\n{state['J1_Defi']}")
        if role == "B":
            if st.button(f"✅ Valider {params.get('n1')}"):
                st.session_state["just_validated"] = True
                st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                nt = random.choice(params.get_all("lb"))
                push_state(nt, random.choice(obtenir_defis(nt, "Mixte")), state['J2_Trait'], state['J2_Defi'], state.get('J1_Score', 0)+1, state.get('J2_Score', 0), state['J1_PW'], state['J2_PW'])
                time.sleep(0.5)
                st.rerun()

    with c2:
        st.markdown(f"<div class='score-box'>Score {params.get('n2')} : {state.get('J2_Score', 0)}</div>", unsafe_allow_html=True)
        st.warning(f"**CIBLE :** {state['J2_Trait'].upper()}\n\n{state['J2_Defi']}")
        if role == "A":
            if st.button(f"✅ Valider {params.get('n2')}"):
                st.session_state["just_validated"] = True
                st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                nt = random.choice(params.get_all("la"))
                push_state(state['J1_Trait'], state['J1_Defi'], nt, random.choice(obtenir_defis(nt, "Mixte")), state.get('J1_Score', 0), state.get('J2_Score', 0)+1, state['J1_PW'], state['J2_PW'])
                time.sleep(0.5)
                st.rerun()

    if role == "A" and st.sidebar.button("♻️ Reset"):
        st.query_params.clear()
        st.session_state.clear()
        st.rerun()

    time.sleep(3)
    st.rerun()
