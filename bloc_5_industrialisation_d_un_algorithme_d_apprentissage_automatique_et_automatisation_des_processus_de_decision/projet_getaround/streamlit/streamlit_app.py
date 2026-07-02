import streamlit as st
import requests

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
    

    # Pour les données catégorielle (non booléens) on est sur des listes avec l'ensemble des classes disponible
    model_key = st.selectbox("Modèle", ['Citroën', 'Peugeot', 'PGO', 'Renault', 'Audi', 'BMW', 'Ford', 'Mercedes', 'Opel', 'Porsche', 'Volkswagen', 'KIA Motors', 'Alfa Romeo', 'Ferrari', 'Fiat', 'Lamborghini', 'Maserati', 'Honda', 'Nissan', 'Mitsubishi', 'SEAT', 'Subaru', 'Toyota', 'Yamaha'])
    fuel = st.selectbox("Carburant", ['diesel', 'petrol', 'hybrid_petrol', 'electro'])
    paint_color = st.selectbox("Couleur", ['black', 'white', 'red', 'silver', 'grey', 'blue', 'orange', 'beige', 'brown', 'green'])
    car_type = st.selectbox("Type de voiture", ['convertible', 'coupe', 'estate', 'hatchback', 'sedan', 'subcompact', 'suv', 'van'])
    
    # Données catégorielle booléens
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