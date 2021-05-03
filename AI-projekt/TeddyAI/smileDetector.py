import numpy as np
import cv2

faceInfo = []
happy = False

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
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eyesCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(5, 5)
        )

        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=15,
            minSize=(25, 25),
        )
        n += 1
        faceInfo.append(
            {"faces": faces, "eyes": eyes, "smile": smile})

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

    elif n == 25:
        break

cap.release()
cv2.destroyAllWindows()

# DATA CLEANING - Filtrera bort 'false positives' och hitta leenden/inte leenden
faceBools = []
for face in faceInfo:
    x = face['faces'][0][0]
    y = face['faces'][0][1]
    w = face['faces'][0][2]
    h = face['faces'][0][3]
    smileBool = False
    # if face['eyes'] == ():
    #     continue

    for smile in face['smile']:
        # x_s = smile[0]
        y_s = smile[1]
        # w_s = smile[2]
        h_s = smile[3]

        print(y, y_s, (y+h)/2)
        if y <= y_s <= (y+h)/2:
            for px in range(y, y + h_s):
                if px not in range(face['eyes'][0][1], face['eyes'][0][3]):
                    smileBool = True

    faceBools.append(smileBool)

# "VOTING"
if faceBools.count(True) > faceBools.count(False):
    happy = True

if happy:
    print('You are happy! :)')
else:
    print('You are not happy! :(')

print(faceInfo)
print(happy)
