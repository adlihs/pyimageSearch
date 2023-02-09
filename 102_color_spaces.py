import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="/images/image1.png",
                help="path to input image")

args = vars(ap.parse_args())

# load original image
image = cv2.imread(args["image"])
cv2.imshow("RGB", image)

# loop for each indiviudal channels and display them
for (name, chan) in zip(("B","G","R"), cv2.split(image)):
    cv2.imshow(name,chan)

# wait for a keypress
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# loop over each of the individual channels and display them
for (name, chan) in zip(("H","S","V"),cv2.split(hsv)):
    cv2.imshow(name,chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

# convert the image to L*a*b* color space
lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
cv2.imshow("L*a*b*", lab)

# loop over each of the individual channels and display them
for (name, chan) in zip(("L*","a*","b*"), cv2.split(lab)):
    cv2.imshow(name,chan)

cv2.waitKey(0)
cv2.destroyAllWindows()


# show original and grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", image)
cv2.imshow("gray", gray)
cv2.waitKey(0)