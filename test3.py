import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
import argparse
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path yo the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

img1 = imutils.resize(image)
# img2 = img1[197:373,181:300]  #roi of the image


indices = np.where(img1 != [0])
coordinates = zip(indices[0], indices[1])

'''
b_list = []
g_list = []
r_list = []
for (x, y) in coordinates:
    b,g,r = img1[x,y]
    b_list.append(b)
    g_list.append(g)
    r_list.append(g)
'''
xx = list(coordinates)
xx = pd.DataFrame(xx, columns=['x', 'y'])

print(xx)

xx.to_csv('image_position.csv')