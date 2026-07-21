import streamlit as st
import requests
from PIL import Image

# --- Configuration de la page Streamlit ---
# pleine largeur
st.set_page_config(page_title="GetAround Dashboard", layout="wide")

# --- Réduction de l'espace blanc en haut de la page ---
st.markdown("""
    <style>
           .block-container {
                padding-top: 1rem;
            }
    </style>
    """, unsafe_allow_html=True)


#  BARRE DE NAVIGATION (SIDEBAR)

st.sidebar.title("Menu GetAround")
st.sidebar.markdown("Sélectionnez l'outil souhaité :")

# Création des deux choix dans le menu
page = st.sidebar.radio(
    "",
    ["1. Analyse des Retards (Produit)", "2. Optimisation des Prix (ML)"]
)

# Aide à la décision
if page == "1. Analyse des Retards (Produit)":
    st.title("📊 GetAround - Analyse des Retards et Conflits")
    st.markdown("Outil d'aide à la décision pour définir le délai minimum entre deux locations.")
    
    # Affichage des KPIs 
    col1, col2, col3 = st.columns(3)
    col1.metric("Locations achevées", "18 045")
    col2.metric("Conducteurs en retard", "44.1 %")
    col3.metric("Conflits réels (Conversion)", "7.7 %")
    
    st.markdown("---")
    
    # graphique de l'EDA
    st.subheader("Visualisation de l'impact métier")
    
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        st.markdown("**Répartition des retards vs Conflits**")
        try:
            st.image("web_conflit.png", use_container_width=True)
        except:
            st.info("Erreur de chargement de l'image")

    with col_img2:
        st.markdown("**Le Dilemme du Délai (Seuil en minutes)**")
        try:
            st.image("web_seuil.png", use_container_width=True)
        except:
            st.info("Erreur de chargement de l'image")

    st.markdown("---")
    st.markdown("### 🎯 Recommandation métier")
    st.success("**Seuil recommandé : 45 à 60 minutes.** Ce délai offre le meilleur compromis entre la baisse significative des conflits lors des restitutions et le maintien d'une forte disponibilité de la flotte de véhicules pour maximiser les revenus.")


# page ML prédiction
elif page == "2. Optimisation des Prix (ML)":
    
    # URL de l'API déployée sur Hugging Face
    API_URL = "https://gull1979-getaround-api.hf.space/predict"

    # Configuration de l'interface Streamlit
    st.title("🚗 GetAround - Prédiction Tarification Journalière")
    st.markdown("Utilisez ce formulaire pour estimer le prix de location journalier d'un véhicule.")

    # Formulaire pour les variables explicatives
    # des valeurs par défaut sont prédéfinies 
    with st.form("prediction_form"):
        st.subheader("Informations du véhicule")
        
        # Les deux colonnes numériques sont sous la forme de slide de valeurs
        mileage = st.slider("Kilométrage (km)", min_value=0, max_value=400000, value=50000, step=1000)
        engine_power = st.slider("Puissance moteur (cv)", min_value=0, max_value=309, value=120)
        
        # On divise l'espace des menus déroulants en 2 colonnes pour gagner de la hauteur
        col_sel1, col_sel2 = st.columns(2)
        
        with col_sel1:
            model_key = st.selectbox("Modèle", ['Citroën', 'Peugeot', 'PGO', 'Renault', 'Audi', 'BMW', 'Ford', 'Mercedes', 'Opel', 'Porsche', 'Volkswagen', 'KIA Motors', 'Alfa Romeo', 'Ferrari', 'Fiat', 'Lamborghini', 'Maserati', 'Honda', 'Nissan', 'Mitsubishi', 'SEAT', 'Subaru', 'Toyota', 'Yamaha'])
            fuel = st.selectbox("Carburant", ['diesel', 'petrol', 'hybrid_petrol', 'electro'])
            
        with col_sel2:
            paint_color = st.selectbox("Couleur", ['black', 'white', 'red', 'silver', 'grey', 'blue', 'orange', 'beige', 'brown', 'green'])
            car_type = st.selectbox("Type de voiture", ['convertible', 'coupe', 'estate', 'hatchback', 'sedan', 'subcompact', 'suv', 'van'])
        
        # Données catégorielles booléennes
        st.subheader("Options disponibles")
        col1, col2 = st.columns(2)
        with col1:
            private_parking_available = st.checkbox("Parking privé", value=True)
            has_gps = st.checkbox("GPS", value=True)
            has_air_conditioning = st.checkbox("Climatisation", value=False)
        with col2:
            automatic_car = st.checkbox("Boîte automatique", value=False)
            has_getaround_connect = st.checkbox("GetAround Connect", value=False)
            has_speed_regulator = st.checkbox("Régulateur", value=False)
            winter_tires = st.checkbox("Pneus hiver", value=True)

        # méthode streamlit pour le texte du bouton de post à l'api
        submit = st.form_submit_button("Calculer le prix")

    # Catch de l'event clic on button 
    if submit:
        # Construction du dictionnaire des données (Payload)    
        payload = {
            "model_key": model_key,
            "mileage": float(mileage),
            "engine_power": float(engine_power),
            "fuel": fuel,
            "paint_color": paint_color,
            "car_type": car_type,
            "private_parking_available": private_parking_available,
            "has_gps": has_gps,
            "has_air_conditioning": has_air_conditioning,
            "automatic_car": automatic_car,
            "has_getaround_connect": has_getaround_connect,
            "has_speed_regulator": has_speed_regulator,
            "winter_tires": winter_tires
        }
        
        # Appel à l'API via une requête POST
        try:
            response = requests.post(API_URL, json={"input": [list(payload.values())]})
            
            # Vérification du succès de la réponse
            if response.status_code == 200:
                result = response.json()
                st.success(f"### 💰 Prix estimé : {result['prediction'][0]:.2f} € / jour")
            else:
                # Affichage des erreurs en cas d'échec de l'API
                st.error(f"Erreur API ({response.status_code}) : {response.text}")
                
        except Exception as e:
            # Gestion des erreurs de connexion au serveur
            st.error(f"Erreur de connexion : {e}")