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

# cropping an image with OpenCV is accomplished via simple NumPy
# array slices in startY:endY, startX:endX order -- here we are
# cropping the face from the image (these coordinates were
# determined using photo editing such as photoshop,
# gimp, paint, etc)

face = image[84:296, 300:436]
cv2.imshow("Face",face)

# apply another image crop, this time extracting the body
body = image[90:450, 0:290]
cv2.imshow("Body", body)
cv2.waitKey(0)