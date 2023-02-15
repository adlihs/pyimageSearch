import cv2
import numpy as np
import argparse
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path yo the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5),0)
blurred = cv2.Canny(blurred, 1,1)
blurred[np.where(blurred != 0)] = 100
blurred[np.where(blurred == 0)] = 255

indices = np.where(blurred != 255 )
coordinates = zip(indices[0], indices[1])
coordinates = list(coordinates)
coordinates = pd.DataFrame(coordinates, columns=['x', 'y'])

#non_white_pixels = np.column_stack(np.where(gray == 0))

print(coordinates)

coordinates.to_csv('image_position.csv')

cv2.imshow("original", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()