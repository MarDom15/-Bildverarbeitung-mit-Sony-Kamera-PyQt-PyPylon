import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer
from pypylon import pylon
import cv2
import numpy as np
from datetime import datetime
import os

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inspection Caméra Sony - Vision Industrielle")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.image_label = QLabel("Aucune image")
        self.layout.addWidget(self.image_label)

        self.btn_start = QPushButton("Démarrer caméra")
        self.btn_start.clicked.connect(self.start_camera)
        self.layout.addWidget(self.btn_start)

        self.btn_stop = QPushButton("Arrêter caméra")
        self.btn_stop.clicked.connect(self.stop_camera)
        self.btn_stop.setEnabled(False)
        self.layout.addWidget(self.btn_stop)

        self.btn_save = QPushButton("Sauvegarder image annotée")
        self.btn_save.clicked.connect(self.save_image)
        self.btn_save.setEnabled(False)
        self.layout.addWidget(self.btn_save)

        self.setLayout(self.layout)

        self.camera = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.current_frame = None

    def start_camera(self):
        try:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            self.converter = pylon.ImageFormatConverter()
            self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
            self.btn_start.setEnabled(False)
            self.btn_stop.setEnabled(True)
            self.timer.start(30)  # ~33 FPS
        except Exception as e:
            QMessageBox.critical(self, "Erreur caméra", f"Impossible de démarrer la caméra : {e}")

    def stop_camera(self):
        self.timer.stop()
        if self.camera is not None:
            self.camera.StopGrabbing()
            self.camera.Close()
            self.camera = None
        self.image_label.setText("Caméra arrêtée")
        self.btn_start.setEnabled(True)
        self.btn_stop.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.current_frame = None

    def update_frame(self):
        if self.camera is None or not self.camera.IsGrabbing():
            return
        grab_result = self.camera.RetrieveResult(2000, pylon.TimeoutHandling_ThrowException)
        if grab_result.GrabSucceeded():
            image = self.converter.Convert(grab_result)
            img = image.GetArray()
            grab_result.Release()

            # Traitement image (détection objets classiques)
            processed_img = self.process_image(img)

            # Conversion pour affichage Qt
            rgb_image = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(qt_image))

            self.current_frame = processed_img
            self.btn_save.setEnabled(True)
        else:
            grab_result.Release()

    def process_image(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = np.ones((5,5), np.uint8)
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        count_valid = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                count_valid += 1
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                cv2.putText(img, f"Obj {count_valid}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

        cv2.putText(img, f"Objets detects : {count_valid}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        return img

    def save_image(self):
        if self.current_frame is None:
            QMessageBox.warning(self, "Aucune image", "Aucune image à sauvegarder.")
            return
        fname, _ = QFileDialog.getSaveFileName(self, "Enregistrer image", "", "PNG Files (*.png);;JPEG Files (*.jpg)")
        if fname:
            cv2.imwrite(fname, self.current_frame)
            QMessageBox.information(self, "Image sauvegardée", f"Image enregistrée sous : {fname}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec())
