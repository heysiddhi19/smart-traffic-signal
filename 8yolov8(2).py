import cv2
import torch
import time
import threading
import numpy as np
from queue import Queue
from ultralytics import YOLO

# Load optimized YOLOv8 TensorRT model
model = YOLO("yolov8s.trt")  # Runs 10x faster!

# Open video file OR webcam (use 0 for webcam)
cap = cv2.VideoCapture("trafficcongestion.mp4")  # Change to 0 for webcam

# Queue for YOLO detections (Async processing)
frame_queue = Queue()
result_queue = Queue()

# Traffic signal timing
base_time = 10  # Default green light duration (seconds)
max_time = 30   # Max green light duration
active_vehicles = 0
green_light_time = base_time

# Function to run YOLO detection asynchronously
def yolo_inference():
    while True:
        if not frame_queue.empty():
            frame = frame_queue.get()
            results = model(frame, verbose=False)  # TensorRT-powered inference
            result_queue.put(results)

# Start YOLO inference in a separate thread
threading.Thread(target=yolo_inference, daemon=True).start()

# Function to update signal timing dynamically
def update_signal():
    global green_light_time
    while True:
        adjusted_time = min(base_time + (active_vehicles * 2), max_time)
        green_light_time = adjusted_time
        time.sleep(5)  # Update every 5 seconds

# Start signal control in a separate thread
threading.Thread(target=update_signal, daemon=True).start()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if video ends

    # Resize frame for ultra-fast processing
    frame_resized = cv2.resize(frame, (640, 480))

    # Send frame to YOLO queue
    if frame_queue.empty():
        frame_queue.put(frame_resized)

    # Get detection results if available
    if not result_queue.empty():
        results = result_queue.get()

        # Count vehicles (cars, trucks, buses, motorcycles)
        active_vehicles = sum(1 for det in results[0].boxes if det.cls in [2, 3, 5, 7])

    # Display vehicle count and updated signal time
    cv2.putText(frame, f"Vehicles: {active_vehicles}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Green Time: {green_light_time}s", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Show the video
    cv2.imshow("TensorRT Traffic Signal (Ultra-Fast)", frame)

    # Press 'Esc' to exit
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
