import argparse
import cv2
import numpy as np


# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="",
                help="path to the input image")
args = vars(ap.parse_args())

# images are Numpy arrays stored as unsigned 8-bit integers (unit-8)
# with values in the range [0:255]; when using the add/substract
# functions in OpenCV these values will *clipped* to this range,
# even if they fall outside the range [0,255] after applying the
# operation
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print("Max of 255: {}".format(added))
print("Min of 0: {}".format(subtracted))

# using Numpy arithmetic operations (rather than OpenCV operations)
# will result in modulo ("wrap around") instead of being clipped
# to the range [0,255]
added = np.uint8([200]) + np.uint8([100])
subtracted = np.uint8([50]) - np.uint8([100])
print("wrap around: {}".format(added))
print("wrap around: {}".format(subtracted))

# load the original input image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("original", image)

# increaing the pixel in our input image by 100 is
# accomplished by constructing a numpy array that has the * same
# dimensions* as our input image, filling it with ones, multiplying
# it by 100, and then adding the input image and matrix together


M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Lighter", added)

# darker
M = np.ones(image.shape, dtype="uint8") * 50
substracted = cv2.subtract(image, M)
cv2.imshow("darker", substracted)
cv2.waitKey(0)