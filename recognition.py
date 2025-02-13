import cv2
import os
import numpy as np
from deepface import DeepFace

data_path = "dataset/"
known_faces = {}

for file in os.listdir(data_path):
    if file.lower().endswith(('jpg', 'jpeg', 'png')):
        name = os.path.splitext(file)[0]  
        known_faces[name] = os.path.join(data_path, file)

# Initialiser la webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Détection de visages avec OpenCV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        cv2.imwrite("temp_face.jpg", face)
        
        recognized = "Inconnu"
        min_distance = 100  # Seuil de reconnaissance
        
        for name, img_path in known_faces.items():
            try:
                result = DeepFace.verify("temp_face.jpg", img_path, model_name='Facenet', enforce_detection=False)
                if result["distance"] < min_distance:
                    recognized = name
                    min_distance = result["distance"]
            except:
                pass
        
        # Dessiner le rectangle autour du visage
        color = (0, 255, 0) if recognized != "Inconnu" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, recognized, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    cv2.imshow("Face Recognition", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
