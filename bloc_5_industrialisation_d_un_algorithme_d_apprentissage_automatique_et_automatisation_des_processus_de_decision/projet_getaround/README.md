# 🚀 GetAround Project – Delay Analysis & Pricing ML

Plateforme de location de voitures entre particuliers, GetAround fait face aux retards de restitution, impactant la disponibilité pour le locataire suivant. Ce projet apporte deux solutions concrètes pour l'équipe Produit :

* **Gestion opérationnelle** : Analyse des retards et simulation d'un "buffer" (délai minimal) pour minimiser les conflits entre locations.
* **Optimisation tarifaire** : Développement et déploiement d'un modèle de Machine Learning (Random Forest) pour suggérer un prix de location journalier optimal.

*Projet réalisé dans le cadre de la certification Data FullStack – Jedha.*

### 🔗 Livrables :

* **Dashboard Streamlit** : [Accéder au Dashboard](https://gull1979-getaround-dashboard.hf.space/)
* **API Pricing ML** : [Consulter la documentation (Swagger)](https://gull1979-getaround-api.hf.space/docs) ou [Accéder à l'API (/predict)](https://gull1979-getaround-api.hf.space/predict)
* **MLFlow Tracking** : [Visualiser les métriques des modèles](https://gull1979-mlflow-tracking-ft.hf.space/#/experiments/3/runs?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All+Runs&datasetsFilter=W10%3D&compareRunsMode=CHART)

### 🛠 Structure du dépôt

* `/api` : Code source de l'API (FastAPI et Dockerfile).
* `/streamlit` : Dashboard d'analyse (Streamlit) et Dockerfile.
* `/src` : Données brutes utilisées pour l'analyse (get_around_delay_analysis.xlsx, etc.).
* `01_eda.ipynb` : Analyse exploratoire des retards et simulation métier.
* `02_ml.ipynb` : Entraînement et optimisation du modèle de Pricing (Random Forest).

### 💻 Interrogation de l'API (/predict)

Vous pouvez l'interroger comme suit :

**Via curl :**
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"input": [["Renault", 50000.0, 100.0, "petrol", "black", "sedan", 1, 1, 1, 0, 1, 0, 1]]}' https://gull1979-getaround-api.hf.space/predict
```

**Via Python :**
```python
import requests

url = "https://gull1979-getaround-api.hf.space/predict"

response = requests.post(url, json={
    "input": [["Renault", 50000.0, 100.0, "petrol", "black", "sedan", 1, 1, 1, 0, 1, 0, 1]]
})

print(response.json())
```


