# Moving Object Detection with OpenCV

## Project Overview  
This project implements a moving object detection system using OpenCV, a popular computer vision library. It processes video streams or recorded video files to detect and highlight moving objects based on changes between consecutive frames. The system can be used for surveillance, traffic monitoring, and other applications involving motion detection.

## Features  
- Real-time object detection using video input from a camera or video file.  
- Background subtraction to identify moving objects.  
- Bounding boxes drawn around detected moving objects.  
- Adjustable parameters for sensitivity and detection accuracy.

## Technologies Used  
- Python  
- OpenCV  

## How to Run  
1. Clone the repository:  
git clone <repository-url>
cd <repository-directory>


2. Install required libraries:  
pip install -r requirements.txt


3. Run the detection script:  
python detect_moving_objects.py --input <path-to-video-or-camera-index>

text
Use `0` for webcam input.

## Usage  
- The script takes video input, either from a file or webcam, and detects moving objects.  
- Detected objects are highlighted with bounding boxes in the output window.  
- Press 'q' to exit the program.


## Contributing  
Contributions, suggestions, and improvements are welcome! Please open an issue or submit a pull request.
