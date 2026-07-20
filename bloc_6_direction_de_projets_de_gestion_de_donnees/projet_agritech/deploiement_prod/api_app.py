from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import requests

# Initialisation de l'API
app = FastAPI()

MODEL_PATH = "catboost_prod.joblib"
#url du modèle sur S3 (public)
S3_URL = "https://jedha-projet.s3.eu-west-3.amazonaws.com/catboost_prod.joblib"

# Bloc de téléchargement test si le joblib est bien téléchargé
if not os.path.exists(MODEL_PATH):
    try:
        response = requests.get(S3_URL, stream=True)
        response.raise_for_status()
        with open(MODEL_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except Exception as e:
        raise RuntimeError(f"Impossible de récupérer le modèle depuis S3 : {e}")

# Chargement du pipeline global en RAM
pipeline = joblib.load(MODEL_PATH)

# Définition de la structure des données d'entrée attendue (10 features)
class PredictionInput(BaseModel):
    Area: str
    Item: str
    Nutrient_nitrogen_N_total: float
    Nutrient_phosphate_P2O5_total: float
    Nutrient_potash_K2O_total: float
    Fungicides_and_Bactericides: float
    Herbicides: float
    Insecticides: float
    Pesticides_total: float
    Rodenticides: float

@app.post("/predict")
def predict(input_data: PredictionInput):
    # 1. Conversion du JSON reçu en dictionnaire
    data_dict = input_data.model_dump()
    
    # 2. Restructuration des clés pour correspondre EXACTEMENT aux noms des colonnes d'entraînement
    # (Remplace les underscores par les espaces et caractères spéciaux d'origine)
    formatted_dict = {
        "Area": data_dict["Area"],
        "Item": data_dict["Item"],
        "Nutrient nitrogen N (total)": data_dict["Nutrient_nitrogen_N_total"],
        "Nutrient phosphate P2O5 (total)": data_dict["Nutrient_phosphate_P2O5_total"],
        "Nutrient potash K2O (total)": data_dict["Nutrient_potash_K2O_total"],
        "Fungicides and Bactericides": data_dict["Fungicides_and_Bactericides"],
        "Herbicides": data_dict["Herbicides"],
        "Insecticides": data_dict["Insecticides"],
        "Pesticides (total)": data_dict["Pesticides_total"],
        "Rodenticides": data_dict["Rodenticides"]
    }
    
    # 3. Conversion en DataFrame Pandas (conserve l'ordre exact des clés du dictionnaire)
    df_features = pd.DataFrame([formatted_dict])
    
    # 4. Inférence : Calcul de la prédiction via le pipeline global
    prediction = pipeline.predict(df_features)
    
    # 5. Renvoi du résultat converti en type natif Python
    return {"prediction": float(prediction[0])}