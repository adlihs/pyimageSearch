import numpy as np
import argparse
import cv2

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="",
                help="path to the input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
cv2.imshow("original",image)

# a mask is the same size as our image, but has only two pixel
# values, 0 and 255, -- pixels with value of 0 (background) are
# ignored in the original image while mask pixels with a value of
# 255 (foreground) are allowed to be kept
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0,90), (290,450), 255, -1)
cv2.imshow("Rectangular mask", mask)

# apply our mask -- notice how only the person in the image is
# cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to image", masked)
cv2.waitKey(0)

# now lets make a circular mask with a radius of 100 pixels and
# apply the mask again
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask,(365,190),100,255,-1)
masked = cv2.bitwise_and(image, image, mask=mask)
print(image.shape[:2])
cv2.imshow("Circular Mask", mask)
cv2.imshow("Masked Applied to Image", masked)
cv2.waitKey(0)