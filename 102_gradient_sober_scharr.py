import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, required=True,
                help="path to image")
ap.add_argument("-s","--scharr", type=int, default=0,
                help="path to input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# set the kernel size depending on whether we are using the Sobel operator or the Scharr operator
# then compute the gradients along the X and Y axis respectively
ksize = -1 if args["scharr"] > 0 else 3
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

# the gradient magnitude images are now of the floating point data type,
# so we need to take care to convert them back to unsigned 8-bit integer representation
# so other OpenCV function can operate on them and visualize them.
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# combine the gradient representations into a single image
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

# show output images

cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr Y", gY)
cv2.imshow("Sobel/Scharr combined", combined)
cv2.waitKey(0)


