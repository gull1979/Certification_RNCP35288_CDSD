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

### 🚀 Liens de Production & Déploiement

* 📊 **Tracking ML-Flow :** [Afficher les métriques des modèles](https://gull1979-mlflow-tracking-ft.hf.space/#/experiments/2/runs?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All+Runs&datasetsFilter=W10%3D&compareRunsMode=CHART)
* 💾 **Modèle Entraîné (AWS S3) :** [Télécharger catboost_prod.joblib](https://jedha-projet.s3.eu-west-3.amazonaws.com/catboost_prod.joblib)
* 🌍 **Application Web :** [DashBoard AgriTech pour les prédictions de rendement](https://gull1979-api-production.hf.space/)
