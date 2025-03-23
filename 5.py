import cv2

cascade_path = r"C:\project\cars.xml"  # Windows
# cascade_path = "/home/yourname/Downloads/haarcascade_car.xml"  # Linux/Mac

car_cascade = cv2.CascadeClassifier(cascade_path)

if car_cascade.empty():
    print("Error: Cannot load the cascade file! Check the file path.")
else:
    print("Cascade file loaded successfully.")

