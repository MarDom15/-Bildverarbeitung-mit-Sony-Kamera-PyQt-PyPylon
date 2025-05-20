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
```
---

## 🔢 Detailed Processing Steps

### 1. Image Acquisition

* **Camera connection**: via Sony SDK or using GenICam standard (e.g., Aravis, Spinnaker).
* **Triggering**: Hardware or software trigger initiates image capture when an object enters the inspection zone.
* **High-resolution capture**: (e.g., 5MP, 30fps) ensures accurate analysis.
* **Synchronization**: With the conveyor belt to prevent blurred images.

### 2. Image Preprocessing

* **Grayscale conversion**: Reduces data complexity for faster analysis.
* **Contrast equalization**: Histogram equalization improves detail visibility by normalizing lighting across the image.
* **Gaussian filtering**: Reduces noise to minimize false detections.

### 3. Object Segmentation

* **Adaptive thresholding**: Separates foreground (objects) from background, robust against non-uniform lighting.
* **Mathematical morphology**:

  * **Closing (dilation then erosion)**: Fills small holes and connects fragmented object parts.
* **Contour detection**: Using OpenCV `findContours` to extract each object as a distinct shape.

### 4. Object Analysis

* **Counting**: `len(contours)` gives the number of detected objects.
* **Measurements for each contour**:

  * **Area**: Pixel-based surface calculation.
  * **Shape**: Aspect ratio (width/height), circularity.
  * **Orientation**: Main angle of object to check alignment.
  * **Positioning**: Compared to a defined tolerance zone in the image.
* **Defect detection**:

  * **Missing objects** (incorrect count).
  * **Deformed shapes** (shape outside tolerance).
  * **Misaligned objects** (outside expected position).

### 5. Logic Output

* If `object_count == expected` **AND** `shape` and `position` are OK →

  * Send **OK status** to PLC (conveyor continues).
* Else →

  * Send **NOK status**, raise alert, **stop conveyor**.
* **Real-time communication**: Via API to the industrial PLC.

### 6. Display and Logging

* **Annotated image**: Rectangles and IDs overlaid on detected objects.
* **CSV logging**: Stores timestamp, object count, and status.
* **NOK image saving**: Faulty images stored in a dedicated folder for later review.
* **Optional dashboard**: For operator supervision and monitoring.

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

For technical support or inquiries, please contact mdomche@gmail.com.


