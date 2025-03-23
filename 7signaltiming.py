import torch
import cv2
import time
import threading

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Open a video file OR webcam (use 0 for webcam)
cap = cv2.VideoCapture("trafficcongestion.mp4")  # Change to 0 for webcam

# Traffic signal timing variables
base_time = 10  # Default green light duration (seconds)
max_time = 30   # Maximum green light duration
vehicle_count = 0
green_light_time = base_time

# Function to update signal timing dynamically
def update_signal():
    global green_light_time
    while True:
        adjusted_time = min(base_time + (vehicle_count * 2), max_time)
        green_light_time = adjusted_time
        time.sleep(5)  # Update signal timing every 5 seconds

# Start signal control in a separate thread
threading.Thread(target=update_signal, daemon=True).start()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if video ends

    # Perform YOLOv5 inference (real-time detection)
    results = model(frame)

    # Count vehicles (cars, trucks, buses, motorcycles)
    vehicle_count = sum(1 for det in results.xyxy[0] if results.names[int(det[5])] in ['car', 'truck', 'bus', 'motorcycle'])

    # Display vehicle count and updated signal time
    cv2.putText(frame, f"Vehicles: {vehicle_count}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Green Time: {green_light_time}s", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Show the video
    cv2.imshow("Adaptive Traffic Signal", frame)

    # Press 'Esc' to exit
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

