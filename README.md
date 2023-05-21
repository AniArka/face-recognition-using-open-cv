# face-recognition-using-open-cv

This project demonstrates how to perform face detection using OpenCV (Open Source Computer Vision Library) and Python. It utilizes the Haar cascade classifier, a machine learning object detection algorithm, to identify and locate human faces in an image or video.

## Requirements
To run this project, you need to have the following:

Python 3.x: Install Python from the official website (https://www.python.org) or using a package manager like Anaconda (https://www.anaconda.com).

OpenCV: Install OpenCV library using pip:

'pip install opencv-python'

## Usage
Clone the repository or download the project files to your local machine.

Open a terminal or command prompt and navigate to the project directory.

Run the following command to execute the program:

python main.py

The program will use the default webcam to capture live video and detect faces in real-time. You can adjust the scaleFactor and minNeighbors parameters in the detect_faces function within the face_detection.py file to fine-tune the face detection algorithm.

Press the 'Esc' key to stop the program.

## Configuration
The 'face_detection.py' file contains a few configuration options that you can modify:

'CASCADE_FILE': Path to the Haar cascade XML file used for face detection. By default, it uses 'haarcascade_frontalface_default.xml', which is included in the project directory.

'SCALE_FACTOR': Parameter specifying how much the image size is reduced at each image scale. You can experiment with different values to achieve better results.

'MIN_NEIGHBORS': Parameter specifying how many neighbors each candidate rectangle should have to retain it. Higher values result in fewer detections but with higher quality.

'MIN_SIZE': Minimum possible object size. Objects smaller than this size will be ignored.

## References
OpenCV documentation: https://docs.opencv.org
Cascade Classifier Training: http://docs.opencv.org/trunk/dc/d88/tutorial_traincascade.html
