import numpy as np
import argparse
import cv2

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="",
                help="path to the input image")
args = vars(ap.parse_args())

# load the input image and grab each channel --  note how openCV
# represents images as NumPy arrays with channels in Blue, Green,
# Red ordering rather than red, green, blue
image = cv2.imread(args["image"])
(B,G,R) = cv2.split(image)

# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merged the image back together again
merged = cv2.merge([B,G,R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros,zeros,R]))
cv2.imshow("Green", cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue", cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)