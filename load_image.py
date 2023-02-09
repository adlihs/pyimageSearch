import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

# load image
# height x width = num rows x num columns
image = cv2.imread(args["image"])
(h,w,c) = image.shape[:3]

# display the image width, height and number
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channel: {}".format(c))

# show the image and wait for a key press
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image back to disk
cv2.imwrite("newimage.jpg", image)
