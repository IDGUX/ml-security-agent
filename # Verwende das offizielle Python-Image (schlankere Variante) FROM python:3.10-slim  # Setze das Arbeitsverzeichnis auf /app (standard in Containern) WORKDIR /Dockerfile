# Verwende das offizielle Python-Image (schlankere Variante)
FROM python:3.10-slim

# Setze das Arbeitsverzeichnis auf /app (standard in Containern)
WORKDIR /app

# Kopiere alle Dateien in den Container
COPY . .

# Installiere Systempakete (falls nötig) und Python-Abhängigkeiten
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Setze den Startbefehl für den Container
CMD ["python3", "/app/ml_security.py"]
x