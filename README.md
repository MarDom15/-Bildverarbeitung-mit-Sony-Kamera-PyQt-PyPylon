# Object Detection and Counting System for Packaging using Sony Camera

---

## 🎯 Objective

This project aims to design an industrial system capable of automatically detecting, counting, and verifying objects placed on a conveyor belt before packaging. Using a high-resolution Sony camera combined with advanced image processing, the system ensures:

- All expected objects are present.
- Objects are undamaged and meet shape criteria.
- Objects are correctly positioned within a tolerance zone.

The goal is to ensure packaging quality and avoid any incidents due to missing, damaged, or misaligned items.

---

## 🔧 Hardware Used

- **Sony XCG / XCL Series Camera**  
  High-resolution industrial camera with GigE or Camera Link interface, ensuring fast and accurate image capture.

- **Diffuse LED Lighting / Backlight**  
  Provides uniform or backlit illumination, facilitating object segmentation and detection.

- **Industrial or Embedded PC**  
  Handles real-time image processing, equipped with Python and required libraries.

---

## 💡 Software and Libraries

- **Python 3.x**  
  Main programming language used for development.

- **OpenCV**  
  For image processing, segmentation, and analysis.

- **NumPy**  
  For matrix manipulation and numerical operations.

- **PyPylon (Sony SDK)**  
  Interface with the Sony industrial camera.

- **Pandas**  
  For data management and result logging.

- **Tkinter**  
  For a simple graphical user interface (GUI) for monitoring and control.

---

## ⚙️ Detailed Technical Pipeline

### 🔁 Pipeline Diagram

```text
┌───────────────┐
│   Sony Camera │
│ (via PyPylon) │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│  Image        │
│  Acquisition  │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│ Preprocessing │
│ - Grayscale   │
│ - Equalize    │
│ - Gaussian    │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│ Segmentation  │
│ - Threshold   │
│ - Morphology  │
│ - Contours    │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│ Object        │
│ Analysis      │
│ - Count       │
│ - Shape       │
│ - Position    │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│ Logic Output  │
│ - OK / NOK    │
│ - PLC Alert   │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│ GUI + Logging │
│ CSV + NOK Img │
└───────────────┘

---
## 🧪 Technical Steps

### Image Acquisition

Automatically triggered capture using SDK as soon as an object enters the inspection zone.

### Preprocessing

* Conversion to grayscale
* Histogram equalization
* Gaussian blur to reduce noise

### Segmentation

* Adaptive thresholding
* Morphological closing to isolate objects

### Object Analysis

* Counting
* Surface calculation
* Orientation and position validation

### Logic Output

* Compares with expected count and tolerances
* Output: OK or NOK status

### Result Display & Logging

* Annotated image output
* CSV logs
* NOK images saved for later analysis

---

## 🧠 Real-World Use Cases

### Medical Kit Packaging

Ensures all required components are present before sealing.

### Logistics / Warehousing

Verifies that all small items are in the parcel before closing the box.

### Food Industry

Accurate product counting before shrink wrapping or boxing.

---

## 🚀 Installation & Requirements

1. Install Python 3.x (recommended: version 3.8+).

2. Install required Python libraries:

```bash
pip install opencv-python numpy pandas pypylon pillow
```

3. Connect the Sony camera via GigE or Camera Link.

4. Set up Sony SDK and ensure camera detection via PyPylon.

5. Set up appropriate lighting for consistent visual conditions.

---

## 🔄 Communication with PLC

The system can be integrated with industrial automation through standard protocols:

* **Profinet**
* **Modbus TCP**

This allows real-time status (OK/NOK) reporting and sending control signals (e.g. stop conveyor).

---

## ⚙️ Customization & Extensions

* Adjust thresholding, size filters, and tolerance zones for different objects.
* Integrate machine learning models for more complex object classification.
* Add a more advanced GUI for operators and system monitoring.
* Automate lighting calibration to adapt to environment changes.

---

## 📁 Project Structure

* `main.py` : Main script handling acquisition, processing, and UI (not included here).
* `output/` : Logging folder

  * `nok_images/` : Stores images with detected errors.
  * `results.csv` : CSV log of processed items and statuses.

---

## 🤝 Contribution

Feel free to propose improvements, report issues, or suggest new features via issues or pull requests.

---

## 📞 Contact

For technical support or inquiries, please contact the project team.
