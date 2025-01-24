import tkinter as tk
from tkinter import Button, Canvas, PhotoImage
import cv2
from PIL import Image, ImageTk
import numpy as np
from tensorflow import keras

# Charger le modèle CNN pré-entraîné
CNN_model = keras.models.load_model('C:/Users/HP/Desktop/BADS 2023-2024/Semestre 1/M12 Projet Data science/Projet RAF-DB DATASET/best_model.h5')  

# Charger le détecteur de visage Haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Dictionnaire pour mapper les indices des émotions aux noms d'émotions
label_dict = {0:'Surprise',1:'Fear',2:'Disgust',3:'Happy',4:'Sad',5:'Angry',6:'Neutral'}

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Test du Modèle CNN avec détection de visage")

# Capture vidéo en utilisant OpenCV
cap = cv2.VideoCapture(0)  # 0 pour la caméra par défaut

#vidéo en utilisant OpenCV
#cap = cv2.VideoCapture('video.mp4')  

# Fonction pour mettre à jour le flux vidéo
def update():
    ret, frame = cap.read()

    # Effet miroir - inverser horizontalement l'image
    frame = cv2.flip(frame, 1)
        
    if ret:
        # Détection de visage
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        
        for (x, y, w, h) in faces:
            # Extraire la région du visage
            face_roi = frame[y:y+h, x:x+w]

            # Prétraitement de l'image pour être compatible avec le modèle CNN
            img = cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (100, 100))  # Assurez-vous de redimensionner l'image selon les exigences du modèle
            img = img / 255.0  # Normaliser les valeurs des pixels
            img = np.expand_dims(img, axis=0)  # Ajouter une dimension pour le lot

            # Prédire la classe de l'image
            prediction = CNN_model.predict(img)
            predicted_class = np.argmax(prediction)

            # Mettre à jour l'étiquette avec la prédiction
            #label_var.set(f"Prédiction : {label_dict[predicted_class]}")
            # Afficher le texte de prédiction
            cv2.putText(frame, f"Emotion: {label_dict[predicted_class]}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # Dessiner les rectangles autour des visages détectés
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Mettre à jour l'affichage de la vidéo
        img = cv2.resize(frame, (640, 480))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        video_canvas.img = img
        video_canvas.create_image(0, 0, anchor=tk.NW, image=img)

    # Mettre à jour la vidéo après un certain délai en millisecondes (ajustez selon vos besoins)
    video_canvas.after(10, update)

# Étiquette pour afficher la prédiction
label_var = tk.StringVar()
prediction_label = tk.Label(root, textvariable=label_var, font=('Helvetica', 14))
prediction_label.pack(pady=10)

# Canvas pour afficher le flux vidéo
video_canvas = Canvas(root, width=640, height=480)
video_canvas.pack()

# Bouton pour quitter l'application
quit_button = Button(root, text="Quitter", command=root.destroy)
quit_button.pack(pady=10)

# Lancer la mise à jour du flux vidéo
update()

# Démarrer la boucle principale Tkinter
root.mainloop()

# Libérer la capture vidéo à la fermeture de la fenêtre
cap.release()
