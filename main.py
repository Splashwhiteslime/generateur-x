import streamlit as st
import random
import importlib

# Liste exacte de vos fichiers (basée sur vos images)
TRAITS = [
    "pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", 
    "audacieux", "soumis", "dominant", "souple", "sportif", 
    "timide", "coquin", "voyeur", "romantiaue", "esclave", 
    "gourmand", "intello", "sournois", "menteur"
]

st.set_page_config(page_title="Générateur X", page_icon="🔥")

st.title("🔥 Générateur X")

# Identification simple par appareil
nom = st.text_input("Entre ton prénom pour commencer :")
sexe = st.radio("Ton sexe :", ["M", "F"], horizontal=True)

if nom:
    st.write(f"Bonjour **{nom}**, prêt(e) pour un défi ?")
    
    if st.button("🎲 TIRER MON DÉFI PERSONNALISÉ"):
        # Sélection d'un trait au hasard
        trait_nom = random.choice(TRAITS)
        module = importlib.import_module(trait_nom)
        
        # On tire un défi (Mode Mixte par défaut)
        defis = module.get_defis("Mixte")
        choix = random.choice(defis)
        
        # Affichage avec accord en genre
        st.session_state.resultat = f"📍 **DÉFI {trait_nom.upper()} :** \n\n {choix}"

    if 'resultat' in st.session_state:
        st.info(st.session_state.resultat)

st.write("---")
st.caption("Partagez l'URL de cette page avec votre partenaire pour jouer ensemble !")