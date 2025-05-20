# 🎯 Industrielle Bildverarbeitung mit Sony-Kamera – PyQt & PyPylon

Dieses Projekt implementiert eine grafische Benutzeroberfläche in Python zur Live-Bildaufnahme  
und Analyse mit einer industriellen Sony-Kamera, die GenICam unterstützt, unter Verwendung der PyPylon-Bibliothek.

---

## Funktionen

- Live-Videoaufnahme mit Sony-Kamera (GigE/USB3 Vision-kompatibel)  
- Klassische Bildverarbeitung (Binärisierung, Morphologie, Konturenerkennung)  
- Markierung erkannter Objekte im Bild  
- Echtzeit-Anzeige der Anzahl erkannter Objekte  
- Speicherung annotierter Bilder im PNG/JPEG-Format über die GUI  
- Einfache Benutzeroberfläche mit PyQt6

---

## Voraussetzungen

- Python 3.7 oder höher  
- OpenCV (`opencv-python`)  
- PyPylon (`pypylon`)  
- PyQt6 (`PyQt6`)

---

## Installation




# 🖥️ Nutzung

## 1. Kamera anschließen  
Schließe deine Sony-Kamera (GigE oder USB3 Vision) per Ethernet oder USB an.

## 2. Skript starten  

## 3. Funktionen in der Oberfläche  
- **Démarrer caméra** – Startet den Live-Stream der Kamera  
- **Arrêter caméra** – Beendet die Kameraverbindung  
- **Sauvegarder image annotée** – Speichert das aktuell verarbeitete Bild mit Markierungen

⚠️ Die Oberfläche ist bewusst einfach gehalten, aber funktional und realistisch einsetzbar im industriellen Kontext.

---

## 🧠 Verwendete Algorithmen (klassische Bildverarbeitung)

- Graustufen-Konvertierung (cv2.cvtColor)  
- Weichzeichnung (cv2.GaussianBlur)  
- Otsu-Schwellenwert (cv2.threshold)  
- Morphologische Operationen (cv2.morphologyEx)  
- Konturenerkennung (cv2.findContours)  
- Objektauswahl via Flächenfilter (cv2.contourArea)  

Diese Methoden sind gut geeignet für einfache bis mittlere Kontrollaufgaben in der Produktion, z. B.:

✅ Zählen von Produkten auf einem Förderband  
✅ Prüfen, ob Objekte vollständig sind  
✅ Erkennung von fehlenden oder defekten Teilen  

---

## 🧪 Getestete Umgebung

- Windows 10 + Sony XCG-CG510 (GigE Vision)  
- Ubuntu 22.04 + Kamera über Aravis (alternativ zu PyPylon möglich)  
- Python 3.11, OpenCV 4.8, PyQt6  

---

## 📝 Beispiel: Anwendungsszenario in der Industrie

**Projekt:** Objektzählung auf einer Verpackungslinie  
**Hardware:** Sony GigE-Kamera, oberhalb des Förderbandes montiert  

### Ablauf:
- Kamera wird über die GUI gestartet  
- Bilder werden in Echtzeit aufgenommen  
- Das System erkennt und zählt Objekte automatisch  
- Bilder mit Markierungen werden auf Wunsch gespeichert  
- Integration möglich mit SPS oder Robotik (optional)  

---

## 👤 Autor

**Dein Name**  
📧 mdomche@gmail.com  
🔗 https://github.com/MarDom15  

---

## 📝 Lizenz

Dieses Projekt steht unter der MIT-Lizenz – freie Nutzung für persönliche oder kommerzielle Projekte unter Beibehaltung des Copyright.

---

## 🧩 Erweiterungsmöglichkeiten

- 🔌 Integration von Trigger-Eingängen (z. B. für SPS)  
- 🧠 Erweiterung mit Deep Learning-Modulen (z. B. YOLOv8, TensorRT)  
- 🎥 Multi-Kamera-Support  
- 📤 Export von Ergebnissen (CSV, MQTT, OPC UA)  

---

## 📸 Screenshots (optional)

(Hier kannst du Screenshots deiner GUI oder von Erkennungsergebnissen einfügen)
