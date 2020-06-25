import cv2
face_cascade = cv2.CascadeClassifier(
    r"C:\Users\Rahesh R\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
img = cv2.imread("front_face.jpg")
#aimg = cv2.resize(img, (300, 300))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(face_cascade.load("haarcascade_frontalface_default.xml"))
face = face_cascade.detectMultiScale(grey, 1.05, 5)
for x, y, w, h in face:
    img = cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 3)

cv2.imshow("image", img)
print(img.shape)
cv2.waitKey(0)
