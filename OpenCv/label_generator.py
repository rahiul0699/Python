import os
import numpy as np
from PIL import Image
import cv2 as cv
import pickle
current_id = 0
x_train = []
y_label = []
label_id = {}
recognizer = cv.face.LBPHFaceRecognizer_create()
face_cascade = cv.CascadeClassifier(
    r"C:\Users\Rahesh R\Desktop\Python\Project\OpenCv\data\haarcascade_frontalface_alt2.xml")
Base_Dir = os.path.dirname(__file__)
Image_Dir = os.path.join(Base_Dir, "images")
for root, dir, files in os.walk(Image_Dir):
    for file in files:
        if file.endswith('jpg') or file.endswith('png') or file.endswith('jpeg'):
            loc = os.path.join(root, file)
            label = os.path.basename(root)
            print(label, loc)
            if label in label_id:
                pass
            else:
                label_id[label] = current_id
                current_id = current_id+1
            id = label_id[label]
            image = Image.open(loc).convert("L")
            image_array = np.array(image, "uint8")
            face = face_cascade.detectMultiScale(
                image_array, scaleFactor=1.5, minNeighbors=5)
            for x, y, w, h in face:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_label.append(id)


with open('lablel.pickle', 'wb') as f:  # pickle helps to convert the objects into a specifoed file
    pickle.dump(label_id, f)

recognizer.train(x_train, np.array(y_label))
recognizer.save('trainner.yml')
