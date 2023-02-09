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
(h,w) = image.shape[:2]
cv2.imshow("Original",image)

# images are simply Numpy arrays -- with the origin (0,0) located at
# the top-left of the image
(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

# access the pixel located at x=50, y=20
(b,g,r) = image[20,50]
print("Pixel at (50,20) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

# update the pixel at (50,20) and set it to red
image[20,50] = (0,0,255)
(b,g,r) = image[20,50]
print("Pixel at (50,20) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

# compute the center of the image which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)
print("Center X:",cX)
print("Center Y:", cY)
# since we are using Numpy arrays we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the
# top-left corner of the image
tl = image[0:cY, 0:cX] # image[startY:endY, startX:endX]
cv2.imshow("Top-left corner", tl)

# in a similar fashion we can crop the top-right, bottom-right, and
# bottom-left corners of the image and then display them to our
# screen
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom Left corner", bl)

# set the top-left corner of the original image to be green
image[0:cY, 0:cX] = (0,255,0)

# show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)