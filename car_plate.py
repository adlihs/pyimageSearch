import numpy as np
import cv2

# read in image
img = cv2.imread('images/car_plate2.jpg')

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply adaptive threshold
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

# find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]

# loop through contours
for cnt in contours:

    # approximate the contour
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)

    # if number of sides is 4, then it is a rectangle
    if len(approx) == 4:

        #check for size of the rectangle
        (x,y,w,h) = cv2.boundingRect(cnt)
        if w > 70 and h > 40:
            # draw rectangle around car plate
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

# show result
cv2.imshow('Car Plate Detection',img)
cv2.waitKey(0)