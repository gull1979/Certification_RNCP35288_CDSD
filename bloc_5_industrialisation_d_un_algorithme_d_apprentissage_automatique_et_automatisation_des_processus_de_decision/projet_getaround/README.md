🚀 GetAround Project – Delay Analysis & Pricing ML

Plateforme de location de voitures entre particuliers, GetAround fait face aux retards de restitution, impactant la disponibilité pour le locataire suivant. Ce projet apporte deux solutions concrètes pour l'équipe Produit :

    Gestion opérationnelle : Analyse des retards et simulation d'un "buffer" (délai minimal) pour minimiser les conflits entre locations.

    Optimisation tarifaire : Développement et déploiement d'un modèle de Machine Learning (Random Forest) pour suggérer un prix de location journalier optimal.

Livrables :

    Dashboard interactif : Visualisation des impacts business (taux de blocage vs conflits résolus).

    API de prédiction : Endpoint /predict déployé et documenté, permettant d'intégrer le modèle en production.

Projet réalisé dans le cadre de la certification Data FullStack – Jedha.


🔗 Livrables :

    Dashboard Streamlit : Lancer la prédiction avec l'ensemble des paramètres de tarification
	
		https://gull1979-getaround-dashboard.hf.space/

    API Pricing ML : API de prédiction de prix (/predict).

        Documentation technique (Swagger) : https://gull1979-getaround-api.hf.space/docs

🛠 Structure du dépôt

    /api : Code source de l'API (FastAPI et Dockerfile.

    /streamlit : Dashboard d'analyse (Streamlit) et Dockerfile.

    /src : Données brutes utilisées pour l'analyse (get_around_delay_analysis.xlsx, etc.).

    01_eda.ipynb : Analyse exploratoire des retards et simulation métier.

    02_ml.ipynb : Entraînement et optimisation du modèle de Pricing (Random Forest).

💻 Interrogation de l'API (/predict)

Vous pouvez l'interroger comme suit :

Via curl :
Bash

curl -i -H "Content-Type: application/json" -X POST \
-d '{"input": [[50000, 120, "Renault", "diesel", "black", "sedan", true, true, false, false, false, false, true]]}' \
https://gull1979-getaround-api.hf.space/predict

Via Python :
Python

import requests

response = requests.post("https://gull1979-getaround-api.hf.space/predict", json={
    "input": [[50000, 120, "Renault", "diesel", "black", "sedan", True, True, False, False, False, False, True]]
})
print(response.json())