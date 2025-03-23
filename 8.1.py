from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8s.pt")  # Change to 'yolov8n.pt' for even faster speed

# Export model to ONNX format
model.export(format="onnx")
