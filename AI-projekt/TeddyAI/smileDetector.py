# Program för att identifiera leenden och bedöma humör.

import numpy as np
import cv2
import os
import random

faceInfo = []  # Listan med data från varje "bild"
happy = False  # Booleanskt värde som säger om personen är glad eller ej
limit = 40  # Begränsar hur många "bilder" som tas
title = ''  # För bildens fönster
db_path = 'AI-projekt/TeddyAI/db/'  # För att hitta rätt bild

# Hitta fler HAAR-cascades om du vill leka mer med detta: https://github.com/opencv/opencv/blob/master/data/haarcascades/
faceCascade = cv2.CascadeClassifier(
    'AI-projekt/Cascades/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier(
    'AI-projekt/Cascades/haarcascade_smile.xml')
eyesCascade = cv2.CascadeClassifier(
    'AI-projekt/Cascades/haarcascades_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)  # Live videofeed från kamera
cap.set(3, 1920)  # set Width
cap.set(4, 1080)  # set Height

n = 0
while True:
    # Data för leenden och ögon
    eyelist = []
    smileList = []

    # Läs av videon och gör den grå för AI:ns skull
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Hittar ansikten
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # x = x-position, y = y-position, w = bredd, h = höjd
    for x, y, w, h in faces:

        # Skala av resten så bilden bara kollar inuti ansiktets ram
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

        # För varje ansikte lägger man till en "bild" med datan.
        n += 1
        faceInfo.append(
            {"faces": faces, "eyes": eyes, "smile": smile})

    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # press 'ESC' to quit
        break

    elif n == limit:
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

    for smile in face['smile']:
        # x_s = smile[0]
        y_s = smile[1]
        # w_s = smile[2]
        h_s = smile[3]

        # Kolla om leendets y-position finns i den undre halvan av ansiktet
        if y <= y_s <= round(y+h/2):
            for pos in range(y, y + h_s):
                try:
                    # Se till så att leendet inte sitter i ögonhöjd (extra säkerhet)
                    if pos not in range(face['eyes'][0][1], face['eyes'][0][3]):
                        smileBool = True
                except IndexError as e:
                    # Ibland är ögon-arrayen tom, och då kan vi ju inte kontrollera ögonen, så programmet antar att leendet är korrekt.
                    if not face['eyes']:
                        smileBool == True

    faceBools.append(smileBool)

# "VOTING"
if faceBools.count(True) > faceBools.count(False):
    happy = True

# RESULTAT
if happy:
    print('\nYou are happy! :)')
else:
    print('\nYou are not happy! :(')

# För att få någon sort procentsats som man kan använda och säga "Du är med 67% säkerhet glad" till exempel.
if happy:
    certainty = round((faceBools.count(True) / len(faceBools))*100)
else:
    certainty = round((faceBools.count(False) / len(faceBools))*100)

print(f'  - Predicted with {certainty}% certainty')

# REKOMMENDATIONER: Lokal "databas" för exempel.
if happy:
    title = 'Happy :)'
    # Om användaren är glad kommer hela pathen se ut ungefär så här: "AI-projekt/TeddyAI/db/happy/"
    db_path += 'happy/'
else:
    title = 'Not Happy :('
    db_path += 'not_happy/'

# Tar mappens (antingen 'happy/' eller 'not_happy/') innehåll och slumpar en bild.
file = db_path + random.choice(os.listdir(db_path))

# Läser bilden från den genererade pathen och öppnar ett fönster där det står om man är glad eller inte.
img = cv2.imread(file)
cv2.imshow(title, img)

# Utan detta kommando skulle fönsstret stängas direkt
key = cv2.waitKey(0)
if key == '27':
    cv2.destroyAllWindows()  # press ESC to exit
