import cv2

# Initialize the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("Webcam is working. Press 'q' to exit.")

# Create a named window and set it to fullscreen mode
cv2.namedWindow('Webcam Feed', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Webcam Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Continuously capture frames from the webcam
while True:
    ret, frame = cap.read()  # Capture frame-by-frame

    if not ret:
        print("Failed to grab frame.")
        break

    # Display the frame in fullscreen mode
    cv2.imshow('Webcam Feed', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
