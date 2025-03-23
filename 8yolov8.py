import cv2
import torch
import time
import threading
import numpy as np
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv8 model (faster than YOLOv5)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Switch to yolov8 if available

# Initialize DeepSORT Tracker
tracker = DeepSort(max_age=30)  # Tracks objects over time

# Open a video file OR webcam (use 0 for webcam)
cap = cv2.VideoCapture("trafficcongestion.mp4")  # Change to 0 for webcam

# Traffic signal timing variables
base_time = 10  # Default green light duration (seconds)
max_time = 30   # Maximum green light duration
active_vehicles = 0  # Tracked vehicles in real time
green_light_time = base_time

# Background function to update signal timing
def update_signal():
    global green_light_time
    while True:
        adjusted_time = min(base_time + (active_vehicles * 2), max_time)
        green_light_time = adjusted_time
        time.sleep(5)  # Update signal timing every 5 seconds

# Start signal control in a separate thread
threading.Thread(target=update_signal, daemon=True).start()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if video ends

    # Perform YOLOv5 inference
    results = model(frame)

    # Extract detections: (x1, y1, x2, y2, confidence, class)
    detections = []
    for det in results.xyxy[0]:  
        x1, y1, x2, y2, conf, cls = det
        label = results.names[int(cls)]
        if label in ['car', 'truck', 'bus', 'motorcycle']:
            detections.append(([int(x1), int(y1), int(x2), int(y2)], conf, label))

    # Track vehicles using DeepSORT
    tracks = tracker.update_tracks(detections, frame=frame)

    # Count actively tracked vehicles
    active_vehicles = sum(1 for track in tracks if track.is_confirmed())

    # Display vehicle count and updated signal time
    cv2.putText(frame, f"Tracked Vehicles: {active_vehicles}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Green Light: {green_light_time}s", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Draw tracking IDs
    for track in tracks:
        if not track.is_confirmed():
            continue
        x1, y1, x2, y2 = map(int, track.to_ltwh())
        track_id = track.track_id
        cv2.rectangle(frame, (x1, y1), (x1 + x2, y1 + y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {track_id}", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the video
    cv2.imshow("Smart Traffic Signal (YOLOv8 + DeepSORT)", frame)

    # Press 'Esc' to exit
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
