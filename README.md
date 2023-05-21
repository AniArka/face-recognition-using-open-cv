# face-recognition-using-open-cv

This project is a face recognition attendance system that uses OpenCV, NumPy, and the face_recognition library to detect and recognize faces in a webcam feed. It captures frames from the webcam, detects faces, and matches them against a set of known faces.

## Prerequisites
* Python (version X.X.X)
* OpenCV (version X.X.X)
* NumPy (version X.X.X)
* face_recognition 

## Installation
1. Clone the repository:

git clone https://github.com/AniArka/face-recognition-using-open-cv.git

2. Navigate to the project directory:

cd project

3. Install the required dependencies:

pip install opencv-python numpy face-recognition

## Usage
1. Open the folder named imageattendance in the project directory.

Place the images of the individuals whose attendance you want to track inside the imageattendance folder. Each image should contain a single face.

2. Run the application:

python main.py

3. The webcam feed will open, and faces detected in real-time will be compared against the known faces provided. If a match is found, the person's name will be displayed on the screen.

4. Press the 'q' key to exit the application.

## Configuration
No additional configuration is required for this project.

## Contributing
Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository (git clone https://github.com/your-username/project.git).
3. Create a new branch for your feature or bug fix (git checkout -b feature/your-feature).
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to the branch on your forked repository.
6. Submit a pull request to the main repository's master branch.

Please ensure that your code adheres to the project's coding conventions and includes any necessary tests.
