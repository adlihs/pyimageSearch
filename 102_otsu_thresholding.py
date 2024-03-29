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


# apply Otsu's automatic thresholding which automatically determines the best threshold value
(T, threshInv) = cv2.threshold(blurred, 0, 255,
                               cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))

# visualize only the masked regions in the image
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("output", masked)
cv2.waitKey(0)