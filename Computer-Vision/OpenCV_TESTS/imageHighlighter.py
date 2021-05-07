# DESC: OPTION TO CHOOSE AREA OF IMAGE AND SELECT COLOR CHANNEL (OR BLACK AND WHITE)

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog


# GET IMAGE & OPEN IMAGE

# img = np.zeros((1000, 1000, 3), np.uint8)
path = 'AI-projekt/TeddyAI/db/happy/YouHappy.jpg'
img = cv2.imread(path)


# GET MOUSE POSITION
points = []


def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 255), -1)
        points.append((x, y))
        if len(points) == 2:
            width = points[1][0] - points[0][0]
            height = points[1][1] - points[0][1]

            ROI = img[x:x+width, y:y + height]
            ROI = cv2.cvtColor(ROI, cv2.COLOR_BGRA2GRAY)
            points.clear()

        cv2.imshow(path.split("/")[-1], img)


cv2.imshow(path.split("/")[-1], img)


cv2.setMouseCallback(path.split("/")[-1], clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()

# GET COLOR CHANNEL

# CALCULATE SQAURE

# SQUARE ROI

# CHANGE ROI COLORS

# SHOW RESULTS
