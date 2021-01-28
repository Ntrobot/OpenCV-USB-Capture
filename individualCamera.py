import cv2
import time

deviceId = 0

cap = cv2.VideoCapture(deviceId)

if not(cap.isOpened()):
	print("Could not open the camera")

else:
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
	cap.set(cv2.CAP_PROP_FPS, 45)
	
	
	retOne, frameOne = cap.read()
	cv2.imwrite("1.jpg", frameOne)
	
	time.sleep(10)
	
	retTwo, frameTwo = cap.read()
	cv2.imwrite("2.jpg", frameTwo)
	
	time.sleep(10)
	
	retThree, frameThree = cap.read()
	cv2.imwrite("3.jpg", frameThree)
	
		

