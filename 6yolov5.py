import torch
import cv2
import numpy as np

# Load YOLOv5 model (pre-trained on COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Open a video file OR webcam (use 0 for webcam)
cap = cv2.VideoCapture("trafficcongestion.mp4")  # Change to 0 for webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if video ends

    # Convert frame to RGB (YOLOv5 expects RGB format)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform inference
    results = model(img_rgb)

    # Extract detections (bounding boxes, labels, confidence scores)
    for det in results.xyxy[0]:  
        x1, y1, x2, y2, conf, cls = det  # Bounding box and class info
        label = results.names[int(cls)]  # Get class name

        # Only detect vehicles (cars, trucks, buses, motorcycles)
        if label in ['car', 'truck', 'bus', 'motorcycle']:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the output video
    cv2.imshow("YOLOv5 Vehicle Detection", frame)

    # Press 'Esc' to exit
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
