from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
import os       
import requests 

# Initialisation de l'API
app = FastAPI(
    title="GetAround Tarification",
    description="API de prédiction des prix de location de véhicules"
)

# chargement du modèle
MODEL_PATH = "getaround_rforest_opt.joblib"
#url du modèle sur S3 (public)
S3_URL = "https://certification-getaround.s3.eu-west-3.amazonaws.com/getaround_rforest_opt.joblib"

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

# Définition de la structure des données d'entrée attendue (11 au total)
class PredictionRequest(BaseModel):
    input: list[list] 

@app.post("/predict")
def predict(data: PredictionRequest):
    #Liste des noms de colonnes exacts utilisés lors de la partie développement
    columns = [
        "model_key", "mileage", "engine_power", "fuel", "paint_color", 
        "car_type", "private_parking_available", "has_gps", 
        "has_air_conditioning", "automatic_car", "has_getaround_connect", 
        "has_speed_regulator", "winter_tires"
    ]
    
    # Passage par un dataframe en entrée du modèle
    df = pd.DataFrame(data.input, columns=columns)
    
    # Envoi du DF au patern
    prediction = pipeline.predict(df)
    
    # Retour correspondant à la prédiction de la target "rental_price_per_day"
    return {"prediction": prediction.tolist()}

@app.get("/")
async def root():
    return {
        "message": "Bienvenue sur l'API de prédiction GetAround",
        "documentation": "Rendez-vous sur /docs pour voir les endpoints disponibles.",
        "status": "online"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)