
import numpy as np
import cv2

# initialize our canvas as 300x300 pixel image with 3 channels
# (red, Green and Blue) with a black background

canvas = np.zeros((300,300,3), dtype="uint8")

# draw a green line from the top-left corner of our canvas to the
# bottom right

green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

# draw a 3 pixel thick red line from top-right corner to the
# bottom-left
red = (0,0,255)
cv2.line(canvas, (300,0),(0,300),red,3)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# draw a red rectangle this one red with 5 pixel thickness
cv2.rectangle(canvas,(50,200),(200,225),red,5)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# draw a blue rectangle (blue and filled in)
blue = (255,0,0)
cv2.rectangle(canvas,(200,50),(225,125),blue,-1)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# re initialize oir canvas as aempty array, then compute
# center (x,y) coordinates of the canvas
canvas = np.zeros((300,300,3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255,255,255)

# ----- CIRCLE ------ #
# loop over increasing radii, from 25 pixels to 150 pixels in 25
# pixel increments
for r in range(0,175,25):
    # draw a white circle
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# re initialize the canva
canvas = np.zeros((300,300,3), dtype="uint8")

# lets draw 25 random circles
for i in range(0,25):
    # randomly generate a radius size between 5 and 200, generate
    # random color, and then pick a random point on our canvas where
    # the circle will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0,high=256, size=(3,)).tolist()
    pt = np.random.randint(0,high=300, size=(2,))

    cv2.circle(canvas, tuple(pt), radius, color,-1)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
