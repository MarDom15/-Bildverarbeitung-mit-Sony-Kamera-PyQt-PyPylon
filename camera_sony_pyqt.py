import cv2
import numpy as np
import pandas as pd
import os
import datetime
from pypylon import pylon
from tkinter import Tk, Label, Button, Canvas, PhotoImage
from PIL import Image, ImageTk

# Configuration constants
EXPECTED_COUNT = 3  # Expected number of objects
TOLERANCE_ZONE = (100, 100, 400, 400)  # Acceptable object area (ROI)
SAVE_DIR = "output/nok_images"  # Directory to save NOK images
CSV_LOG = "output/results.csv"  # Path to CSV log

# Ensure output directories exist
os.makedirs(SAVE_DIR, exist_ok=True)

# Initialize the CSV log file if it doesn't exist
if not os.path.exists(CSV_LOG):
    df = pd.DataFrame(columns=["timestamp", "count", "status"])
    df.to_csv(CSV_LOG, index=False)

def log_result(timestamp, count, status):
    """Append inspection results to CSV log."""
    df = pd.read_csv(CSV_LOG)
    df.loc[len(df)] = [timestamp, count, status]
    df.to_csv(CSV_LOG, index=False)

def analyze_frame(frame):
    """Process the frame and determine if object count/shape/position is acceptable."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    blurred = cv2.GaussianBlur(equalized, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
    kernel = np.ones((5, 5), np.uint8)
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Find contours (possible objects)
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ok = True
    annotated = frame.copy()

    for idx, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area < 500:  # Filter out noise
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cx, cy = x + w // 2, y + h // 2

        # Check if object is within allowed area
        if not (TOLERANCE_ZONE[0] < cx < TOLERANCE_ZONE[2] and TOLERANCE_ZONE[1] < cy < TOLERANCE_ZONE[3]):
            ok = False

        # Annotate object on image
        cv2.rectangle(annotated, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(annotated, str(idx + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    object_count = len(contours)
    if object_count != EXPECTED_COUNT:
        ok = False

    status = "OK" if ok else "NOK"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Save NOK images for inspection
    if status == "NOK":
        cv2.imwrite(f"{SAVE_DIR}/{timestamp}.png", annotated)

    log_result(timestamp, object_count, status)
    return annotated, status

class MonitoringUI:
    """Simple GUI using Tkinter to show results and interact with camera."""
    def __init__(self, master):
        self.master = master
        master.title("Object Detection Monitoring")

        self.canvas = Canvas(master, width=640, height=480)
        self.canvas.pack()

        self.status_label = Label(master, text="Status: Waiting...", font=("Arial", 14))
        self.status_label.pack()

        self.update_button = Button(master, text="Capture Frame", command=self.capture_and_update)
        self.update_button.pack()

        self.image_on_canvas = None

        # Initialize Sony industrial camera
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.camera.Open()

        # Convert raw image to OpenCV BGR
        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    def capture_and_update(self):
        """Capture frame from camera, process it, and update GUI."""
        self.camera.StartGrabbingMax(1)
        grab_result = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grab_result.GrabSucceeded():
            image = self.converter.Convert(grab_result)
            frame = image.GetArray()

            # Analyze the frame
            analyzed, status = analyze_frame(frame)

            self.status_label.config(text=f"Status: {status}")

            # Display processed frame
            img = Image.fromarray(cv2.cvtColor(analyzed, cv2.COLOR_BGR2RGB))
            img = img.resize((640, 480))
            imgtk = ImageTk.PhotoImage(image=img)

            if self.image_on_canvas is None:
                self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw", image=imgtk)
            else:
                self.canvas.itemconfig(self.image_on_canvas, image=imgtk)
            self.canvas.image = imgtk  # Prevent garbage collection

        grab_result.Release()

# Start the GUI app
if __name__ == "__main__":
    root = Tk()
    app = MonitoringUI(root)
    root.mainloop()
