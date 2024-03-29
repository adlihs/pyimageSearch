import numpy as np
import cv2

# draw a rectangle
rectangle = np.zeros((300,300), dtype="uint8")
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# draw circle
circle = np.zeros((300,300), dtype="uint8")
cv2.circle(circle, (150,150), 150, 255, -1)

cv2.imshow("circle", circle)

# a bitwise 'AND' is only 'True' when both inputs have a value that
# is "ON" -- in this case, the cv2.bitwise_and function examines
# every pixel in the rectangle and circle, if *BOTH* pixels have a
# value greater than zero then the pixel is turned 'ON' (i.e. 255)
# in the output image; otherwise the output value is set to
# 'OFF' (i.e. 0)
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# a bitwise 'OR' examines every pixel in the two inputs and if
# *EITHER* pixel in the rectangle or cirlce is greather than zero,
# then the output has a value of 255, otherwise it is 0
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# the bitwise 'XOR' is identical to the 'OR' function with one
# exception: both the rectangle and circle are not allowed to *BOTH*
# have values greather than 0 (only one can be 0)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# finally the bitwise 'NOT' inverts the values of the pixels, pixels
# with a value 255 become 0 and pixels with a value 0 become 255
bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)