import argparse
import imutils
import cv2

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="",
                help="path to the input image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
cv2.imshow("original", image)

# grab dimensions of the image and calculate the center of the
# image
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX,cY), 45, 1.0) # 45 (positive value) rotate the image clock-wise
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated 45 degrees", rotated)
cv2.waitKey(0)

# rotate our image by -90 degrees around the image
M = cv2.getRotationMatrix2D((cX,cY),-90,1.0)
rotated = cv2.warpAffine(image, M,(w,h))
cv2.imshow("Rotated -90 degrees", rotated)
cv2.waitKey(0)

# rotate our image around an arbitrary point rather than center
M = cv2.getRotationMatrix2D((10,10), 45, 1.0)
rotated =  cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by arbitrary point", rotated)
cv2.waitKey(0)

# use our imutils function to rotate an image 180 degrees
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotated)
cv2.waitKey(0)

# rotate our image by 33 degreees counterclockwise ensuring the
# entire rotated image still views in the viewing area
rotated = imutils.rotate_bound(image,-33)
cv2.imshow("Rotated without cropping", rotated)
cv2.waitKey(0)