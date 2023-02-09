import argparse
import cv2

# contruct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="/Users/edmundneil/PycharmProjects/pyimageSearch/images/image1.png",
                help="path to the input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])

# draw eyes and mouth
cv2.circle(image, (360,188),90, (0,0,255),2)
cv2.circle(image, (350,174),10, (0,0,255),-1)
cv2.circle(image, (388,174),10, (0,0,255),-1)
cv2.rectangle(image, (134,210),(368,218),(0,0,255),-1)

cv2.imshow("output",image)
cv2.waitKey(0)