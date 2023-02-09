import cv2

# Load the video file
cap = cv2.VideoCapture('images/penal.mp4')

# Loop through each frame of the video
while True:
    # Read the next frame
    ret, frame = cap.read()

    # If we have reached the end of the video, break the loop
    if not ret:
        break

    # Pre-process the frame (optional)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    # Find the contours of the soccer field
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

    # Extract the soccer field by drawing a rectangle around its contours
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    # Display the extracted soccer field
    cv2.imshow('Soccer Field', frame)

    # Wait for the user to press a key
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
