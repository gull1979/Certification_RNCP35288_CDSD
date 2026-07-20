# Start with a lightweight Linux Anaconda image
FROM continuumio/miniconda3:25.3.1-1

# Update all packages and install nano unzip and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    nano \
    unzip \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# --- STARTUP SCRIPT PREPARATION (Granting execution rights via Root) ---
# Set the initial working directory while still running as the root user
WORKDIR /home/user/app

# Leverage layer caching: copy only reqs first
COPY requirements.txt requirements.txt

# RUN AS ROOT: Install dependencies inside the global conda environment
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# THIS IS SPECIFIC TO HUGGINFACE
# We create a new user named "user" with ID of 1000
RUN useradd -m -u 1000 user

# Copy all local files to /home/user/app with "user" as owner of these files
# Always use --chown=user when using HUGGINGFACE to avoid permission errors
COPY --chown=user . /home/user/app

# Make the startup script executable to prevent "Permission denied" errors later
RUN chmod +x start.sh

# CORRECTION DROITS ÉCRITURE : Donne la propriété complète du dossier de travail à l'utilisateur pour autoriser le téléchargement S3
RUN chown -R user:user /home/user/app

# We switch from "root" (default user when creating an image) to "user" 
USER user

# We set two environmnet variables 
# so that we can give ownership to all files in there afterwards
# we also add /home/user/.local/bin in the $PATH environment variable 
# PATH environment variable sets paths to look for installed binaries
# We update it so that Linux knows where to look for binaries if we were to install them with "user".
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# We set working directory to $HOME/app (<=> /home/user/app)
WORKDIR /home/user/app

# THIS IS SPECIFIC TO HUGGINGFACE AS WELL
# expose port 7860 which is the port used by HuggingFace for Web Application
EXPOSE 7860

# FORCE STREAMLIT TO RUN WITHOUT WRITING TO THE HOME DIRECTORY
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
    STREAMLIT_TELEMETRY_DISABLE=true

# Run entrypoint script to launch both API and Streamlit
CMD ["./start.sh"]