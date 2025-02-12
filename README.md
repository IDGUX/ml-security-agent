# 🚀 ML-Security-Agent – Anomalie-Erkennung für UniFi Netzwerke

[![MIT License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

**ML-Security-Agent** ist ein **Machine-Learning-gestütztes Intrusion Detection System (IDS)** für **UniFi Netzwerke**.  
Das Skript überwacht den Netzwerkverkehr, erkennt **ungewöhnliches Verhalten** und meldet verdächtige Aktivitäten **automatisch** über einen **Webhook an n8n**.

---

## 🔥 **Funktionen**
✅ **Überwacht den Netzwerkverkehr von UniFi-Clients**  
✅ **Nutzt Machine Learning (Isolation Forest), um Anomalien zu erkennen**  
✅ **Speichert erkannte Bedrohungen in einer SQLite-Datenbank**  
✅ **Sendet Warnungen an einen n8n-Webhook für weitere Automatisierungen**  
✅ **Ignoriert bekannte Geräte & verhindert Fehlalarme**  

---

## 🛠 **Installation**
### **1️⃣ Voraussetzungen**
- **Python 3.8+**
- **UniFi Controller mit API-Zugang**
- **n8n für Webhook-Verarbeitung (optional)**  

### **2️⃣ Repository klonen**
git clone https://github.com/deinusername/ml-security-agent.git
cd ml-security-agent


### Abhängigkeiten installieren
pip install -r requirements.txt


### .env Datei mit API-Keys erstellen
UNIFI_API_URL=https://deincontroller.local/proxy/network/api/s/default/stat/sta
UNIFI_API_KEY=DEIN_API_KEY
N8N_WEBHOOK_URL=http://n8n:5678/webhook/security-alert


### 🚀 Starten
python main.py

### 🤖 Webhook-Integration mit n8n
docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n

Danach kannst du n8n im Browser öffnen:
👉 http://localhost:5678

2️⃣ Webhook-Trigger einrichten
Erstelle einen neuen Workflow in n8n.
Füge einen "Webhook"-Trigger hinzu.
Setze die Methode auf POST.
Kopiere die Webhook-URL und füge sie in .env ein.
Jetzt empfängt n8n automatisch Warnungen von ML-Security-Agent! 🚀

### 📡 API-Datenquelle – UniFi
Falls du die API testen willst, kannst du den Request manuell mit curl ausführen:
curl -H "X-API-KEY: DEIN_API_KEY" -H "Accept: application/json" \
     https://deincontroller.local/proxy/network/api/s/default/stat/sta


## 🛡 Sicherheitshinweise
Speichere deinen API-Key NICHT direkt im Code! Verwende stattdessen die .env Datei.
Falls du Docker nutzt, stelle sicher, dass keine sensiblen Daten im Container-Log gespeichert werden.
Nutze eine Firewall, um nur autorisierte IPs auf die UniFi API zugreifen zu lassen.


📌 To-Do & Weiterentwicklung
 Weitere Machine Learning Modelle testen
 Live-Dashboard für Netzwerküberwachung
 Integration mit Telegram für Benachrichtigungen
 Mehr Netzwerkmetriken zur Analyse hinzufügen
Falls du Ideen oder Verbesserungsvorschläge hast, starte einen Issue oder Pull Request! 😊🚀


⚖ Lizenz
Dieses Projekt steht unter der MIT-Lizenz – du kannst es nutzen, verändern und verbessern!


