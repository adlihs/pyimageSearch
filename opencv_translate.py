import numpy as np
import cv2
import argparse
import imutils

# construct argument
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="",
                help="path to the input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

# shift the image 25 pixels to right and 50 pixels down
M = np.float32([[1,0,25],[0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted downd and right", shifted)
cv2.waitKey(0)

# now lets shift the image 50 pixels to the left and 90 pixels
# up by specifing negative values for the x and y directions
# respectively

M = np.float32([[1,0,-50],[0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left", shifted)
cv2.waitKey(0)

# use the imutils helper function to translate the image 100 pixels
# down in a signle function
shifted = imutils.translate(image,0,100)
cv2.imshow("shifted down", shifted)
cv2.waitKey(0)