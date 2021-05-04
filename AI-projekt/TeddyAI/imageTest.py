# PROGRAM SOM TEST FÖR LOKALT EXPERIMENT!
import os
import random
import cv2

happy = True
title = ''
path = 'AI-projekt/TeddyAI/db/'


if happy:
    title = 'Happy :)'
    path += 'happy/'
else:
    title = 'Not Happy :('
    path += 'not_happy/'

file = path + random.choice(os.listdir(path))
img = cv2.imread(file)

cv2.imshow(title, img)
key = cv2.waitKey(0)

if key == '27':
    cv2.destroyAllWindows()
