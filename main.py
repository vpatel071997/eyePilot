import cv2
import dlib
import numpy as np
import pyautogui
from imutils import face_utils
import kagglehub
import os

# Download latest version of dataset
dataset_dir = kagglehub.dataset_download("sergiovirahonda/shape-predictor-68-face-landmarksdat")
dat_file = os.path.join(dataset_dir, "shape_predictor_68_face_landmarks.dat")

# Initialize dlib's face detector and facial landmark predictor
face_detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(dat_file)

# Get screen size
screen_width, screen_height = pyautogui.size()

# Start video capture
cap = cv2.VideoCapture(0)

# Helper function to get eye center

def get_eye_center(eye_points):
    x = int(np.mean(eye_points[:, 0]))
    y = int(np.mean(eye_points[:, 1]))
    return (x, y)

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)
    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)
        left_eye = shape[36:42]
        right_eye = shape[42:48]
        left_center = get_eye_center(left_eye)
        right_center = get_eye_center(right_eye)
        # Draw eyes
        cv2.circle(frame, tuple(left_center), 3, (0,255,0), -1)
        cv2.circle(frame, tuple(right_center), 3, (0,255,0), -1)
        # Use average of both eyes for cursor
        eye_center = np.mean([left_center, right_center], axis=0)
        # Map eye position to screen
        x_ratio = eye_center[0] / frame.shape[1]
        y_ratio = eye_center[1] / frame.shape[0]
        screen_x = int(screen_width * x_ratio)
        screen_y = int(screen_height * y_ratio)
        pyautogui.moveTo(screen_x, screen_y, duration=0.1)
        # Simple blink detection for click (eye aspect ratio)
        def eye_aspect_ratio(eye):
            A = np.linalg.norm(eye[1] - eye[5])
            B = np.linalg.norm(eye[2] - eye[4])
            C = np.linalg.norm(eye[0] - eye[3])
            return (A + B) / (2.0 * C)
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        EAR_THRESHOLD = 0.21
        if left_ear < EAR_THRESHOLD and right_ear < EAR_THRESHOLD:
            pyautogui.click()
    cv2.imshow('Eye Mouse Control', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
