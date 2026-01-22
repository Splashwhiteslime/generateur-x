import streamlit as st
import random, pandas as pd, time, firebase_admin, string
from firebase_admin import credentials, firestore
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION ---
TRAITS_DISPO = ["pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", "audacieux", "soumis", "dominant", "souple", "sportif", "timide", "coquin", "voyeur", "romantique", "esclave", "gourmand", "intello", "sournois", "menteur"]

st.set_page_config(page_title="Divine Pulse", page_icon="🔥", layout="wide")

# --- AUDIO & STYLE PREMIUM ---
SOUND_NOTIF = "https://www.soundjay.com/buttons/sounds/button-3.mp3"
SOUND_MODIF = "https://www.soundjay.com/buttons/sounds/beep-07a.mp3"
SOUND_VALID = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"

st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%); color: #e0e0e0; }}
    div.stButton > button:first-child {{ 
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%); 
        color: white; border-radius: 15px; font-weight: bold; border: none; height: 3.5em; width: 100%;
    }}
    .score-box {{ background: rgba(0, 0, 0, 0.4); border: 2px solid #ff416c; border-radius: 15px; padding: 15px; text-align: center; color: #ff416c; font-weight: 800; font-size: 22px; margin-bottom: 10px; }}
    .stAlert {{ background: rgba(255, 255, 255, 0.05) !important; backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1) !important; color: white !important; }}
    .alert-modif {{ background-color: rgba(255, 193, 7, 0.2); color: #ffc107; padding: 10px; border-radius: 10px; border: 1px solid #ffc107; text-align: center; font-weight: bold; }}
    </style>
    <audio id="notif-sound" src="{SOUND_NOTIF}" preload="auto"></audio>
    <audio id="modif-sound" src="{SOUND_MODIF}" preload="auto"></audio>
    <audio id="valid-sound" src="{SOUND_VALID}" preload="auto"></audio>
""", unsafe_allow_html=True)

# --- CONNEXIONS ---
if not firebase_admin._apps:
    fb_dict = dict(st.secrets["firebase"])
    cred = credentials.Certificate(fb_dict)
    firebase_admin.initialize_app(cred)
db = firestore.client()
conn_sheets = st.connection("gsheets", type=GSheetsConnection)

def obtenir_un_defi(trait, genre):
    try:
        df = conn_sheets.read(worksheet="Sheet1", ttl=5)
        mask = (df['Trait'].str.lower() == trait.lower()) & (df['Genre'].isin([genre, "Tous"]))
        return random.choice(df[mask]['Défi'].tolist())
    except: return "Fais un bisou à ton partenaire"

# --- LOGIQUE D'ACCUEIL ---
params = st.query_params
room_id = params.get("room")
role_auto = params.get("role")

if "mode" not in st.session_state and not room_id:
    st.title("🔥 Divine Pulse")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🆕 Créer une nouvelle Session"):
            st.session_state.mode = "creation"; st.rerun()
    with col2:
        if st.button("🔌 Se connecter à une Session"):
            st.session_state.mode = "connexion"; st.rerun()
    st.stop()

# --- MODE CRÉATION ---
if st.session_state.get("mode") == "creation":
    st.title("🛡️ Configurer la Session")
    c_name = st.text_input("Nom de la Session (Unique)")
    c_pass = st.text_input("Mot de passe secret", type="password")
    n1 = st.text_input("Ton Prénom")
    s1 = st.radio("Ton Sexe", ["Homme", "Femme"], horizontal=True)
    n2 = st.text_input("Prénom du partenaire")
    traits_b = st.multiselect(f"Personnalité de {n2} :", TRAITS_DISPO)

    if st.button("🚀 Lancer la Session"):
        if c_name and c_pass and n1 and traits_b:
            doc_ref = db.collection("sessions").document(c_name)
            if doc_ref.get().exists:
                st.error("Ce nom de session existe déjà !")
            else:
                doc_ref.set({
                    "pw_session": c_pass, "n1": n1, "s1": s1, "n2": n2,
                    "traits_de_b": traits_b, "step": 1, "update_ts": time.time(), "last_action": "init"
                })
                st.query_params.room = c_name; st.query_params.role = "A"; st.rerun()
    if st.button("⬅️ Retour"): del st.session_state.mode; st.rerun()
    st.stop()

# --- MODE CONNEXION / AUTH ---
if (st.session_state.get("mode") == "connexion" or room_id) and f"auth_done_{room_id}" not in st.session_state:
    st.title("🔌 Accès Privé")
    l_name = st.text_input("Nom de la Session", value=room_id if room_id else "")
    l_pass = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        doc = db.collection("sessions").document(l_name).get()
        if doc.exists:
            data = doc.to_dict()
            if data['pw_session'] == l_pass:
                st.session_state[f"auth_done_{l_name}"] = True
                st.query_params.room = l_name
                if not role_auto:
                    st.session_state.temp_data = data
                    st.session_state.mode = "select_role"
                st.rerun()
            else: st.error("Mot de passe incorrect.")
        else: st.error("Session introuvable.")
    st.stop()

# --- SÉLECTION DU RÔLE ---
if st.session_state.get("mode") == "select_role":
    data = st.session_state.temp_data
    st.subheader(f"Session : {st.query_params.room}")
    role_choice = st.radio("Qui es-tu ?", [data['n1'], data['n2']])
    if st.button("Confirmer mon identité"):
        st.query_params.role = "A" if role_choice == data['n1'] else "B"
        del st.session_state.mode; st.rerun()
    st.stop()

# --- LOGIQUE DE JEU ---
if room_id:
    doc_ref = db.collection("sessions").document(room_id)
    state = doc_ref.get().to_dict()
    role = st.query_params.get("role")

    # ÉTAPE 1 : SETUP B
    if state.get("step") == 1:
        if role == "B":
            st.title(f"💋 Bienvenue {state['n2']}")
            s2 = st.radio("Ton Sexe", ["Homme", "Femme"], horizontal=True)
            traits_a = st.multiselect(f"Comment décrirais-tu {state['n1']} ?", TRAITS_DISPO)
            if st.button("🔥 Commencer le Jeu"):
                genre = "H/H" if state['s1']=="Homme" and s2=="Homme" else "F/F" if state['s1']=="Femme" and s2=="Femme" else "Mixte"
                t_a, t_b = random.choice(traits_a), random.choice(state['traits_de_b'])
                doc_ref.update({
                    "s2": s2, "traits_de_a": traits_a, "genre": genre,
                    "J1_Trait": t_b, "J1_Defi": obtenir_un_defi(t_b, genre), "J1_Score": 0, "J1_Ready": False,
                    "J2_Trait": t_a, "J2_Defi": obtenir_un_defi(t_a, genre), "J2_Score": 0, "J2_Ready": False,
                    "step": 2, "update_ts": time.time(), "last_action": "start"
                })
                st.rerun()
        else:
            st.info(f"⏳ En attente de {state['n2']}...")
            st.code(f"Lien : https://ton-app.streamlit.app/?room={room_id}&role=B")
            time.sleep(4); st.rerun()

    # ÉTAPE 2 : LE JEU
    elif state.get("step") == 2:
        if state.get("J1_Ready") and state.get("J2_Ready"):
            genre = state['genre']
            t_a = random.choice(state['traits_de_a'])
            t_b = random.choice(state['traits_de_b'])
            doc_ref.update({
                "J1_Trait": t_b, "J1_Defi": obtenir_un_defi(t_b, genre), "J1_Score": state['J1_Score']+1, "J1_Ready": False,
                "J2_Trait": t_a, "J2_Defi": obtenir_un_defi(t_a, genre), "J2_Score": state['J2_Score']+1, "J2_Ready": False,
                "update_ts": time.time(), "last_action": "new_round"
            })
            st.rerun()

        # AUDIO SYNC
        if "lts" not in st.session_state: st.session_state.lts = state['update_ts']
        if state['update_ts'] > st.session_state.lts:
            st.session_state.lts = state['update_ts']
            if "jv" not in st.session_state:
                snd = "modif-sound" if state.get("last_action") == "modif" else "notif-sound"
                st.markdown(f'<script>document.getElementById("{snd}").play();</script>', unsafe_allow_html=True)
            else: del st.session_state["jv"]

        st.title(f"⚡ {state['n1']} & {state['n2']}")
        if state.get("last_action") == "modif": st.markdown('<div class="alert-modif">⚠️ Défi modifié par le partenaire !</div>', unsafe_allow_html=True)

        colA, colB = st.columns(2)
        with colA:
            st.markdown(f"<div class='score-box'>{state['n1']} : {state['J1_Score']} pts</div>", unsafe_allow_html=True)
            st.info(f"**DÉFI :**\n\n{state['J1_Defi']}")
            if state.get("J1_Ready"): st.success("✅ Validé")
            elif role == "B":
                if st.button(f"Valider {state['n1']}"):
                    st.session_state["jv"] = True; st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                    doc_ref.update({"J1_Ready": True, "update_ts": time.time(), "last_action": "valid"}); st.rerun()
                with st.expander("✏️ Modifier"):
                    nt = st.text_area("Nouveau texte pour A :")
                    if st.button("Envoyer A"): doc_ref.update({"J1_Defi": nt, "update_ts": time.time(), "last_action": "modif"}); st.rerun()

        with colB:
            st.markdown(f"<div class='score-box'>{state['n2']} : {state['J2_Score']} pts</div>", unsafe_allow_html=True)
            st.warning(f"**DÉFI :**\n\n{state['J2_Defi']}")
            if state.get("J2_Ready"): st.success("✅ Validé")
            elif role == "A":
                if st.button(f"Valider {state['n2']}"):
                    st.session_state["jv"] = True; st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                    doc_ref.update({"J2_Ready": True, "update_ts": time.time(), "last_action": "valid"}); st.rerun()
                with st.expander("✏️ Modifier"):
                    nt = st.text_area("Nouveau texte pour B :")
                    if st.button("Envoyer B"): doc_ref.update({"J2_Defi": nt, "update_ts": time.time(), "last_action": "modif"}); st.rerun()

        if role == "A" and st.sidebar.button("♻️ Reset Salon"): doc_ref.delete(); st.query_params.clear(); st.rerun()
        time.sleep(4); st.rerun()
