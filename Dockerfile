# Verwende ein Python-Base-Image mit Pip vorinstalliert
FROM python:3.10-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere das gesamte Projekt in den Container
COPY . .

# Aktualisiere Paketlisten und installiere Systemabhängigkeiten (falls benötigt)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Standard-Befehl, um das Skript auszuführen (Anpassen falls notwendig)
CMD ["python", "main.py"]
