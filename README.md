# eyePilot

Control your PC mouse cursor using your eyes and perform clicks with simple gestures (like blinking) using your webcam.

## Features
- Real-time eye tracking using your webcam
- Move mouse cursor with your gaze
- Blink gesture to perform mouse clicks
- Easy setup with Python and KaggleHub

## Requirements
- Python 3.7+
- Webcam
- Packages: opencv-python, dlib, imutils, pyautogui, numpy, kagglehub

## Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/vpatel071997/eyePilot.git
   cd eyePilot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app:
   ```sh
   python main.py
   ```

The required facial landmark model (`shape_predictor_68_face_landmarks.dat`) will be downloaded automatically from Kaggle using KaggleHub.

## Usage
- Look at your screen to move the mouse cursor.
- Blink both eyes to perform a mouse click.
- Press `Esc` to exit the application.

## Notes
- For best results, use in a well-lit environment.
- If you encounter issues with the model download, ensure you have KaggleHub set up and internet access.

## License
MIT
