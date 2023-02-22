import numpy as np
from skimage.exposure import is_low_contrast
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="",
                help="optional path to video file")
ap.add_argument("-t", "--thresh", type=float, default=0.35,
                help="threshold for low contrast")
args = vars(ap.parse_args())

# grab a pointer to the input video stream
print("[INFO] accesing video stream...")
vs = cv2.VideoCapture(args["input"] if args["input"] else 0)

# loop over frames from the video stream
while True:
    # read a frame from the video stream
    (grabbed, frame) = vs.read()

    # if the frame was not grabbed then we have reached the end of the video stream so exit the script
    if not grabbed:
        print("[INFO] no frame read from stream - exiting")
        break

    # resize the frame convert it to grayscale, blur it and then perform edge detection
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)

    # initialize the text and color to indicate that current frame is NOT low contrast
    text = "Low Contrast: No"
    color = (0, 255, 0)

    # check to see if the frame is low contarst and if so, update tje text and color
    if is_low_contrast(gray, fraction_threshold=args["thresh"]):
        text = "Low Contrast: Yes"
        color = (0, 0, 255)
    # otherwise the frame is NOT low contrast so we can continue processing it
    else:
        # find contours in the edge map and find the largest one, which we will assume is the outline of our color
        # correction
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)

        # draw the largest contour on the frame
        cv2.drawContours(frame,[c],-1,(0,255,0),2)

    # Draw the text on the output on the frame
    cv2.putText(frame, text, (5,25), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                color,2)

    # stack the output frame and edge map next to each other
    output = np.dstack([edged] * 3)
    output = np.hstack([frame, output])

    # show the output to our screen
    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key was pressed break from the loop
    if key == ord("q"):
        break
