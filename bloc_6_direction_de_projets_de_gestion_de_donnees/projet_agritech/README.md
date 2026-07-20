### 🎯 Thème

Ce dossier est l'aboutissement du projet de fin de formation FullStack chez **Jedha**. C'est un travail collectif réalisé au sein d'un groupe de 4 personnes.

Nous avons choisi ce sujet en partant d'un jeu de données en provenance de **Kaggle**, que nous avons ensuite approfondi. L'agriculture est un domaine qui nous a fédérés, et faire de la prédiction de rendement de récoltes a été un beau challenge.

---

### 📂 Contenu

Il y a actuellement **3 notebooks** dans ce dépôt. Chronologiquement, ils s'articulent ainsi :

* **`1 - 01_data_merge_for_EDA.ipynb`**
  C'est le point de départ qui fusionne 2 sources :
  * La **FAOstat** (Organisation des Nations Unies pour l'alimentation et l'agriculture)
  * La **CRU** (Unité de recherche Climatique)
  
  > L'agrégation de ces éléments (Pays / Récoltes / Rendement / Nutriments / Pesticides / Climat) sur 124 ans a constitué la base de données initiale.

* **`2 - 02_EDA_26_06_04.ipynb`**
  C'est à cette étape que l'on a mis à plat les données pour leur donner du sens et les rendre compatibles avec l'apprentissage d'un modèle d'IA.

* **`3 - 03_ML_26_06_10.ipynb`**
  Voici la partie apprentissage, avec pas moins de 4 modèles testés et paramétrés pour donner le meilleur d'eux-mêmes.

### ⚙️ Fichiers de Déploiement

* 📁 **[Code source déploiement docker](deploiement_prod/)**
* 📄 [Script python Front - Streamlit](https://github.com/gull1979/Certification_RNCP35288_CDSD/blob/main/bloc_6_direction_de_projets_de_gestion_de_donnees/projet_agritech/deploiement_prod/streamlit_app.py)
* 📄 [Script python API en background](https://github.com/gull1979/Certification_RNCP35288_CDSD/blob/main/bloc_6_direction_de_projets_de_gestion_de_donnees/projet_agritech/deploiement_prod/api_app.py)

### 🚀 Liens de Production & Déploiement

* 📊 **Tracking ML-Flow :** [Afficher les métriques des modèles](https://gull1979-mlflow-tracking-ft.hf.space/#/experiments/2/runs?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All+Runs&datasetsFilter=W10%3D&compareRunsMode=CHART)
* 💾 **Modèle Entraîné (AWS S3) :** [Télécharger catboost_prod.joblib](https://jedha-projet.s3.eu-west-3.amazonaws.com/catboost_prod.joblib)
* 🌍 **Application Web :** [DashBoard AgriTech pour les prédictions de rendement](https://gull1979-api-production.hf.space/)
