import cv2

print("Smart Attendance System - Camera Check")
camera = cv2.VideoCapture(0)

if camera.isOpened():
    print("Camera detected successfully.")
else:
    print("Unable to access camera.")
