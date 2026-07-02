# Utilise l'image Miniconda officielle pour la gestion de l'environnement Python
FROM continuumio/miniconda3:25.3.1-1

# Installation des dépendances système nécessaires au bon fonctionnement de l'API
RUN apt-get update && apt-get install -y --no-install-recommends \
    nano \
    unzip \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Définition du répertoire de travail par défaut
WORKDIR /home/user/app

# Copie préalable des dépendances pour optimiser le cache de Docker (couches)
COPY requirements.txt requirements.txt

# Installation des bibliothèques Python dans l'environnement conda
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Création d'un utilisateur non-root pour des raisons de sécurité (standard Hugging Face)
RUN useradd -m -u 1000 user

# Copie du code source avec attribution des droits de propriété à l'utilisateur 'user'
COPY --chown=user . /home/user/app

# Configuration des droits d'écriture sur le répertoire pour permettre le téléchargement du modèle S3
RUN chown -R user:user /home/user/app

# Passage à l'utilisateur 'user' pour exécuter l'API sans privilèges root
USER user

# Configuration de l'environnement PATH pour inclure les exécutables locaux
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Exposition du port 7860 (obligatoire pour l'accessibilité sur Hugging Face Spaces)
EXPOSE 7860

# Point d'entrée : exécution de l'application Streamlit
CMD ["streamlit", "run", "streamlit_app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]