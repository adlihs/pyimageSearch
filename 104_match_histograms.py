import skimage
import matplotlib.pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True,
                help="Path to the input source image")
ap.add_argument("-r","--reference", required=True,
                help="path to the input reference image")
args = vars(ap.parse_args())

# load the source and reference images
print("[INFO] loading source and reference images...")
src = cv2.imread(args["source"])
ref = cv2.imread(args["reference"])

# determine if we are performing multichannel histogram matching
# and then perform histogram matching itself
print("[INFO] performing histogram matching...")
multi = True if src.shape[-1] > 1 else False # to check how many channels the picture has, if a color image will have 3 channels and will be set it as 'multi', if a gray scale image will not be 'multi'
matched = skimage.exposure.match_histograms(src, ref, multichannel=multi)

# show images
cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)
cv2.waitKey(0)

# construct a figure to display the histogram plots for each channel before and after histogram matching was applied
(fig, axs) = plt.subplots(nrows=3, ncols=3, figsize=(8,8))

# loop over our source image, reference image, and output matched image
for (i,image) in enumerate((src,ref,matched)):
    # convert the image from BGR to RGB channel ordering
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # loop over the names of the channels in RGB order
    for (j, color) in enumerate(("red","green","blue")):
        # compute a histogram for the current channel and plot it
        (hist,bins) = skimage.exposure.histogram(image[..., j],
                                         source_range = "dtype")
        axs[j,i].plot(bins, hist / hist.max())

        # compute the cumulative distribution function for the current channel and plot it
        (cdf, bins) = skimage.exposure.cumulative_distribution(image[..., j])
        axs[j,i].plot(bins, cdf)

        # set the y-axis label of the current plot to be the name of the current color channel
        axs[j,0].set_ylabel(color)

# set the axes titles
axs[0,0].set_title("Source")
axs[0,1].set_title("Reference")
axs[0,2].set_title("Matched")

# display the output plots
plt.tight_layout()
plt.show()
