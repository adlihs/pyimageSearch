import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, required=True,
                help= "path to input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
cv2.imshow("image", image)

# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7),0)
cv2.imshow("Gray and Blurred", blurred)

# apply basic thresholding -- first parameter is the image
# we want to threshold, the second value is our threshold check;
# if a pixel value is greater than our threslhold (in this case 200)
# we set it to be *black*, otherwise it is *white*
(T, threshInv) = cv2.threshold(blurred, 200, 255,
                               cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

# using normal threslholding (rather than inverse thresholding)
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

# visualize only the masked regions in the image
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)
