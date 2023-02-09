import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# construct a rectangular kernel (13x5) and apply a black hat
# operation wich enables us to find a dark regions on a light
# background
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
blackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# similarly, a TopHat (also called "whiteHat") operation will
# enable us to find light regions on a dark background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# show the output images
cv2.imshow("Original", image)
cv2.imshow("BlackHat", blackHat)
cv2.imshow("TopHat", tophat)
cv2.waitKey(0)
