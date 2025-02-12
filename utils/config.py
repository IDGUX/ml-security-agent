import os
from dotenv import load_dotenv

# 🛡️ Umgebungsvariablen laden
load_dotenv()

# 🔧 Basisverzeichnis des Projekts (2 Ebenen nach oben für Modularität)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")

# 📁 Falls "data/" nicht existiert, erstelle es automatisch
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 🔐 API-Keys und URLs
UNIFI_API_URL = os.getenv("UNIFI_API_URL", "https://controller.local/proxy/network/api/s/default/stat/sta")
UNIFI_API_KEY = os.getenv("UNIFI_API_KEY")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "http://n8n:5678/webhook/security-alert")

# 📦 Absolute Dateipfade für die Datenbank und das Modell
MODEL_PATH = os.path.join(DATA_DIR, "isolation_forest_model.pkl")
DB_PATH = os.path.join(DATA_DIR, "network_logs.db")

HEADERS = {
    "X-API-KEY": UNIFI_API_KEY,
    "Accept": "application/json"
}
