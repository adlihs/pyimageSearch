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

# flip image horizontally
print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image,1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
print("[INFO] flipping image vertically...")
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image,-1)
print("[INFO] flipping image horizontally and vertiically...")
cv2.imshow("Flipped Vertically and horizontally", flipped)
cv2.waitKey(0)