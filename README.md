# System Voice Controller

This Python project utilizes computer vision to control a system's voice commands through finger gestures, offering a hands-free interaction experience. It combines gesture recognition algorithms with speech processing, enabling users to navigate and operate the system without physical touch.

## Introduction

This project aims to provide an intuitive and convenient method for controlling system audio using hand gestures detected through a webcam. By employing computer vision techniques, specifically utilizing the MediaPipe library, the program tracks the movements of the user's hand in real-time. It maps these movements to adjust the system's audio volume dynamically, offering a novel and engaging interaction method.

## Features

### Real-time Hand Gesture Detection: 
The system accurately identifies hand gestures using the MediaPipe library, enabling seamless control of system audio.
### Dynamic Volume Adjustment: 
By interpreting the distance between specific hand landmarks, the program adjusts the system's audio volume in real-time.
### User-friendly Interface: 
The application provides visual feedback, displaying the hand gestures and their corresponding actions in real-time, enhancing the user experience.
### Hands-free Operation: 
Users can control the system's audio without the need for physical interaction with any input devices, offering a hands-free and convenient solution.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required libraries by running:

```bash
pip install opencv-python mediapipe pycaw comtypes
```
3. Clone this repository to your local machine.
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the Python script:
```
python system_voice_controller.py
```
6. Position your hand in front of the webcam and perform the specified gestures to control the system's audio volume.
7. Press 'x' to exit the application.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyCaw
- comtypes

## Acknowledgments

- This project utilizes the capabilities of the MediaPipe library for hand tracking and gesture recognition.
- PyCaw is used for interfacing with the Windows Core Audio API to adjust the system's audio volume.
- Special thanks to the developers and contributors of these libraries for their valuable contributions.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per your requirements. Contributions are welcome!
