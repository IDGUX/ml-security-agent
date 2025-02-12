import joblib
import numpy as np
from utils.logger import logger
from utils.config import MODEL_PATH

def save_model(model):
    """Speichert das trainierte Modell."""
    try:
        joblib.dump(model, MODEL_PATH)
        logger.info("✅ Modell gespeichert!")
    except Exception as e:
        logger.error(f"❌ Fehler beim Speichern des Modells: {e}")

def load_model():
    """Lädt das gespeicherte Modell, falls vorhanden."""
    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        return None

def train_model(tx_data):
    """Trainiert das Modell, falls kein Modell vorhanden ist."""
    model = load_model()
    if model is None:
        model = IsolationForest(contamination=0.05)
        model.fit(tx_data)
        save_model(model)
    return model
