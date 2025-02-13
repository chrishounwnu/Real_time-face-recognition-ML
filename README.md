# Real-Time Facial Recognition with Voice Feedback

This project implements a **real-time facial recognition system** using OpenCV and DeepFace, with **voice feedback** to guide users. The system detects and identifies faces in a live webcam feed and provides audio feedback.

## 📌 Features
- **Face Detection & Recognition** using DeepFace (Facenet model).
- **Live Camera Feed** with OpenCV.
- **Voice Feedback** using a text-to-speech module.
- **Real-time Results Display** directly on the webcam feed.
- **Handles Multiple Image Formats** (.jpg, .png, etc.).
- **Unknown Face Handling** (Displays "Unknown" for unrecognized faces).


# Dataset

Put the images in the dataset folder et rename each image 

#Run this project: 

python recognition.py

## 🚀 Installation Guide

### 1️⃣ Create & Activate Virtual Environment
Using **Python's venv**:
```bash
python -m venv env

After this:

- On windows: env\Scripts\activate
- On Linux: source env/bin/activate

2️⃣ Install Dependencies
Ensure you have pip installed, then run:

pip install -r requirements.txt

Important : If you later find missing packages, install them with: pip install package_name
