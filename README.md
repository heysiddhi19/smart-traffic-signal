# smart-traffic-signal
🚦 Smart Traffic Signal
📌 Overview
This project implements a Smart Traffic Signal System using Python, OpenCV, and YOLOv8 for real-time vehicle detection. Instead of static timers, the system dynamically adjusts traffic signals based on vehicle density, improving traffic flow efficiency.

🎯 Features
✅ Real-Time Vehicle Detection with YOLOv8
✅ Adaptive Traffic Light Control based on vehicle count
✅ Python-Based Simulation using video input
✅ OpenCV for Image Processing
✅ Optimized Traffic Management to reduce congestion

🛠️ Technologies & Libraries Used
Programming Language: 🐍 Python

Deep Learning Model: YOLOv8 (Ultralytics)

Libraries Used:

🖼️ OpenCV (Image Processing)

🤖 YOLOv8 (Ultralytics) for object detection

📊 NumPy & Pandas

🔢 PyTorch

🚀 Installation & Usage
🔹 1. Clone the Repository

git clone https://github.com/heysiddhi19/smart-traffic-signal.git
cd smart-traffic-signal

🔹 2. Install Dependencies
Make sure you have Python installed, then run:

pip install -r requirements.txt

🔹 3. Download the YOLOv8 Model
You need to download the YOLOv8 weights for object detection:

pip install ultralytics
yolo download yolo8n.pt  # or use yolo8s.pt for a more accurate model

🔹 4. Run the Traffic Signal Simulation

python main.py

🔹 5. How It Works
The system takes a video feed as input (live camera or recorded).

YOLOv8 detects vehicles in each lane.

The system counts vehicles in different lanes.

The lane with the most traffic gets a longer green signal to ease congestion.

The process repeats dynamically, optimizing traffic flow.

📸 Demo
(Include images or a GIF showcasing the project in action)

🛠️ Customization
Modify YOLO model parameters to adjust detection confidence.

Adjust traffic signal timing logic in the script.

Use live CCTV footage instead of video files for real-world testing.

🏆 Future Enhancements
🌎 Integration with real-world traffic cameras

🚀 TensorRT acceleration for faster detection

📊 Web Dashboard for real-time monitoring

🔗 IoT-based Smart Signal Communication

🤝 Contributing
Contributions are welcome! Feel free to fork the repo, improve it, and submit a pull request.

📜 License
This project is licensed under MIT License.

📢 Need Help?
For any issues, open a GitHub Issue, or reach out via email: siddhisambhav05@gmail.com .

🚀 Made with ❤️ by heysiddhi19

