import cv2

# Load the Haar cascade file (already working now!)
cascade_path = r"C:\project\cars.xml"  # Ensure correct path
car_cascade = cv2.CascadeClassifier(cascade_path)

# Open a video file OR webcam (use 0 for live webcam)
cap = cv2.VideoCapture("trafficvideo.mp4")  # Change to 0 for webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if video ends

    # Convert frame to grayscale (Haarcascades work better in grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the frame
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    # Draw rectangles around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the output video
    cv2.imshow("Car Detection", frame)

    # Press 'Esc' to exit
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
