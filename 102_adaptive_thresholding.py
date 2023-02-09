import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, required=True,
                help= "path to input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
cv2.imshow("image", image)

# convert the to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

# apply adaptive thresholding with a hardcoded threshold value
(T, threshInv) = cv2.threshold(blurred, 230, 255,
                               cv2.THRESH_BINARY_INV)
cv2.imshow("Simple Thresholding", threshInv)
cv2.waitKey(0)

# apply Outsu's automatic thresholding
(T, threshInv) = cv2.threshold(blurred, 0, 255,
                               cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Otsu Thresholding", threshInv)
cv2.waitKey(0)

# Instead of manually specifying the threshold value we can use
# adapative trhresholidng to examine neighborhoods of pixels and
# adaptively threshold each neighborhood
thresh = cv2.adaptiveThreshold(blurred,
                               255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY_INV,
                               21,10)
cv2.imshow("Mean Adaptive Thresholding", thresh)
cv2.waitKey(0)

# perform adapative thresholding again this time using a Gaussian
# weighting versus a simple mean to compute our local threshold value
thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,4)
cv2.imshow("Gaussian Adaptive Thresholding", thresh)
cv2.waitKey(0)



