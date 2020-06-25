import cv2 as cv
import pickle

labels = {}
with open('lablel.pickle', 'rb') as f:
    org = pickle.load(f)
for k, v in org.items():
    labels[v] = k


# print(labels)

face_cascade = cv.CascadeClassifier(
    r"C:\Users\Rahesh R\Desktop\Python\Project\OpenCv\data\haarcascade_frontalface_alt2.xml")
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')
cap = cv.VideoCapture(0)
while True:
    check, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for x, y, w, h in face:
        roi = gray[y:y+h, x:x+h]
        #result = r'C:\Users\Rahesh R\Desktop\Python\Project\OpenCv\result.png'
        #cv.imwrite(result, roi)
        id, conf = recognizer.predict(roi)
        if conf >= 45 and conf <= 85:
            font = cv.FONT_HERSHEY_SIMPLEX
            name = labels[id]
            cv.putText(frame, name, (x, y), font, 2,
                       (255, 0, 255), 2, cv.LINE_AA)

        endcord_x = x+w
        endcord_y = y+h
        thick = 2
        color = (0, 0, 255)
        cv.rectangle(frame, (x, y), (endcord_x, endcord_y), color, thick)

    cv.imshow("Recording", frame)

    key = cv.waitKey(5)
    if key == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
