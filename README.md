# Industrielle Bildverarbeitung mit Sony-Kamera – PyQt & PyPylon

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

```bash
pip install opencv-python pypylon PyQt6
