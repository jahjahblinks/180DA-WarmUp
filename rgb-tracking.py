# CREATED USING BELOW RESOURCE LINKS
# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
# https://cvexplained.wordpress.com/2020/04/28/color-detection-hsv/
# NOT CURRENTLY FUNCTIONING - HSV TECHNIQUE DOES NOT WORK?

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # define range of blue color in RGB
    lower_blue = np.array([0,0,255])
    upper_blue = np.array([0,255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(rgb, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()