import time
import requests
import json
from utils.logger import logger
from utils.config import UNIFI_API_URL, HEADERS, N8N_WEBHOOK_URL
from database.db import init_db, log_anomaly
from models.isolation_forest import train_model
from sklearn.ensemble import IsolationForest

def fetch_unifi_data():
    """Holt die Liste aller verbundenen Clients von der UniFi API."""
    try:
        response = requests.get(UNIFI_API_URL, headers=HEADERS, verify=False)
        if response.status_code != 200:
            logger.error(f"❌ API-Fehler: {response.status_code} - {response.text}")
            return []
        
        data = response.json().get("data", [])
        logger.info(f"📡 API Antwort enthält {len(data)} Clients")
        return data
    except Exception as e:
        logger.error(f"❌ Fehler beim Abrufen der Daten: {e}")
        return []

def analyze_network_data(devices):
    """ML-Analyse zur Erkennung von Anomalien im Netzwerkverkehr."""
    tx_data = []
    client_info = []

    for d in devices:
        mac = d.get("mac", "Unknown")
        hostname = d.get("hostname", mac)
        tx_bytes = d.get("tx_bytes", 0)
        rx_bytes = d.get("rx_bytes", 0)
        last_seen = d.get("last_seen", 0)
        active_connections = d.get("num_conn", 1)
        is_wired = d.get("is_wired", False)

        data_rate = (tx_bytes + rx_bytes) / (time.time() - last_seen) if last_seen > 0 else 0

        tx_data.append([tx_bytes, rx_bytes, active_connections, data_rate])
        client_info.append({
            "device": hostname, "mac": mac, "tx_bytes": tx_bytes, "rx_bytes": rx_bytes,
            "connections": active_connections, "data_rate": data_rate, "last_seen": last_seen,
            "is_wired": is_wired
        })

    if len(tx_data) < 3:
        logger.warning("⚠️ Zu wenige Daten für ML-Analyse")
        return []

    model = train_model(tx_data)
    predictions = model.predict(tx_data)
    alerts = [info for i, info in enumerate(client_info) if predictions[i] == -1]

    if alerts:
        logger.warning(f"🚨 Anomalien erkannt:\n{json.dumps(alerts, indent=2)}")
        send_alerts(alerts)
        for alert in alerts:
            log_anomaly(alert)
    else:
        logger.info("✅ Keine Anomalien erkannt.")

    return alerts

def send_alerts(alerts):
    """Sendet erkannte Anomalien an den n8n-Webhook."""
    if not alerts:
        logger.info("📩 Keine Anomalien zu senden.")
        return

    for alert in alerts:
        payload = {"device": alert["device"], "mac": alert["mac"], "data_rate": alert["data_rate"]}

        try:
            response = requests.post(N8N_WEBHOOK_URL, json=payload)
            if response.status_code == 200:
                logger.info(f"✅ Warnung gesendet: {payload}")
            else:
                logger.error(f"❌ Fehler beim Senden an n8n: {response.status_code} - {response.text}")
        except Exception as e:
            logger.error(f"❌ Fehler beim Senden der Warnung: {e}")

if __name__ == "__main__":
    logger.info("🚀 ML-Security-Agent gestartet!")
    init_db()
    while True:
        devices = fetch_unifi_data()
        analyze_network_data(devices)
        time.sleep(300)
