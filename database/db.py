import sqlite3
from utils.logger import logger
from utils.config import DB_PATH

def init_db():
    """Erstellt die Datenbank falls nicht vorhanden."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS anomaly_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device TEXT,
                    mac TEXT,
                    tx_bytes INTEGER,
                    rx_bytes INTEGER,
                    connections INTEGER,
                    data_rate REAL,
                    last_seen INTEGER,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
        logger.info("✅ Tabellen erfolgreich erstellt!")
    except Exception as e:
        logger.error(f"❌ Fehler beim Erstellen der Datenbank: {e}")

def log_anomaly(info):
    """Speichert erkannte Anomalien in der Datenbank."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO anomaly_logs (device, mac, tx_bytes, rx_bytes, connections, data_rate, last_seen)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (info["device"], info["mac"], info["tx_bytes"], info["rx_bytes"], info["connections"], info["data_rate"], info["last_seen"]))
            conn.commit()
    except Exception as e:
        logger.error(f"❌ Fehler beim Speichern der Anomalie: {e}")
