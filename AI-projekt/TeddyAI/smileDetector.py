import numpy as np
import cv2

faceInfo = []

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
# more cascades: https://github.com/opencv/opencv/blob/master/data/haarcascades/
faceCascade = cv2.CascadeClassifier(
    'AI-projekt/Cascades/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier(
    'AI-projekt/Cascades/haarcascade_smile.xml')
eyesCascade = cv2.CascadeClassifier(
    'AI-projekt/Cascades/haarcascades_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 1920)  # set Width
cap.set(4, 1080)  # set Height

n = 0
while True:
    eyelist = []
    smileList = []

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eyesCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(5, 5)
        )

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 0), 2)

        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=15,
            minSize=(25, 25),
        )

        for xx, yy, ww, hh in smile:
            cv2.rectangle(roi_color, (xx, yy),
                          (xx + ww, yy + hh), (100, 50, 255), 2)
        n += 1
        faceInfo.append(
            {"faces": faces, "eyes": eyes, "smile": smile})

        cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

    elif n == 5:
        break


cap.release()
cv2.destroyAllWindows()

print(faceInfo)
