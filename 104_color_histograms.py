import pandas as pd
from matplotlib import pyplot as plt
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path yo the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# split the image into its respective channels, then initialize the
# tuple of channel names along with our figure for plotting
channels = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# loop over the image channels
for (channels, colors) in zip(channels, colors):
    # create a histogram for the current channel and plot it
    print(colors)
    hist = cv2.calcHist([channels], [0], None, [256], [0, 256])
    hist2 = pd.DataFrame(hist)
    hist2['bin'] = list(range(len(hist2)))
    hist3 = hist2.to_dict(orient="list")
    print(hist2)
    print(hist3)
    plt.plot(hist, color=colors)
    plt.xlim([0, 256])

# create a new figure and then plot a 2D color histogram for the
# green and bkuee channels

fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])

# print(hist.size)
# print(hist)
# x = pd.DataFrame(hist)
# x = x.to_dict(orient="list")
# print(len(x))
# print(x)


p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)
plt.show()

# plot a 2D color histogram for the green and red channels
ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)
plt.show()

# plot a 2D color histogram for blue and red channels
ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
plt.show()

# and finally lets examine the dimensionality of one of the 2D histograms
# print("2D histogram shape: {}, with {} values".format(
# hist.shape, hist.flatten().shape[0]
# ))
