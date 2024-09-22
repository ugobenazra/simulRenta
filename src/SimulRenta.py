
import streamlit as st
import folium
from streamlit_folium import st_folium

from utils import calcul_renta, display_simul 

# Définir les emplacements des appartements avec des coordonnées
appartements = {
    "4 avenue Mozart": {"coords": [48.855390, 2.274703], "prix": 500000, "frais_agence": 10000, "apport": 100000, "taux_emprunt": 3.69, "surface": 50, "charges_copro": 100, "travaux": 1, "meubles": 5000, "assurance_emprunt": 500, "n_annees": 20, "internet": 360, "assurance_proprio": 200, "taxe_fonciere": 1000},
    "10 rue de Buci": {"coords": [48.8534, 2.3370], "prix": 600000, "frais_agence": 12000, "apport": 120000, "taux_emprunt": 1.4, "surface": 60, "charges_copro": 150, "travaux": 1, "meubles": 6000, "assurance_emprunt": 600, "n_annees": 25, "internet": 360, "assurance_proprio": 250, "taxe_fonciere": 1200},
    "39 bd de Belleville": {"coords": [48.8714, 2.3802], "prix": 400000, "frais_agence": 8000, "apport": 80000, "taux_emprunt": 3.2, "surface": 40, "charges_copro": 80, "travaux": 1, "meubles": 4000, "assurance_emprunt": 400, "n_annees": 15, "internet": 360, "assurance_proprio": 180, "taxe_fonciere": 900}
}

# Interface Streamlit
st.title("Simulation de Crédit Immobilier")

# Liste déroulante pour choisir une adresse si non choisie sur la carte
adresse_choisie = st.selectbox("Ou choisissez une adresse :", list(appartements.keys()))

# Obtenir les détails de l'appartement sélectionné
appart_selec = appartements[adresse_choisie]

st.write(f"Vous avez choisi : **{adresse_choisie}**")

# Paramètres du crédit immobilier
apport = st.number_input("Apport (€)", value=appart_selec["apport"])
taux_emprunt = st.number_input("Taux d'emprunt (%)", value=appart_selec["taux_emprunt"])
n_annees = st.number_input("Durée du prêt (années)", value=appart_selec["n_annees"])

# Simuler le crédit immobilier
dic_appart = appart_selec.copy()
dic_appart["apport"] = apport
dic_appart["taux_emprunt"] = taux_emprunt
dic_appart["n_annees"] = n_annees

if st.button("Calculer la rentabilité"):
    result = calcul_renta(dic_appart)
    display_simul(result)