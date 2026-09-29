# Real-Time Automotive Component Detection and Inspection

## 📌 Project Overview

This project presents an AI-based automotive component detection system designed to identify important components inside an automobile engine bay.

The project evaluates and compares three object detection approaches:

- YOLO
- SSD
- Faster R-CNN

The models are evaluated based on detection accuracy, inference speed, and suitability for real-time applications.

The final YOLO model is integrated with OpenCV to perform real-time detection using a webcam.

---

## 🎯 Objectives

The main objectives of this project are:

- Detect automotive engine components using computer vision.
- Train and evaluate YOLO, SSD, and Faster R-CNN.
- Compare model accuracy using mAP, precision, and recall.
- Compare inference speed using FPS.
- Analyze the suitability of each model for real-time applications.
- Implement real-time automotive component detection using a webcam.

---

## 🧠 Models Used

### YOLO

YOLO (You Only Look Once) is used as the primary real-time object detection model.

The trained YOLO model is saved as:


final_automotive_yolo_best.pt

Dataset source:

https://universe.roboflow.com/ahsan-abdullah-omu7t/automotive-engine-part-detection

```text
final_automotive_yolo_best.pt


