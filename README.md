# OpenCV-USB-Capture
Python script to capture images from multiple UVC-compliant (plug and play) USB cameras at once. This repository is created for the Asagao Project at inaho Inc.

## Required dependencies
- sudo apt install v4l-utils
- pip3 install opencv-python==4.5.1.48

## Classes and Methods
### Class Camera
| Method | Parameters | Description |
| --- | --- | --- |
| __init__ | cameraId | Provide camera's ID. This ID can be found with ls /dev/video* |
| setup | N/A | Open the camera, setup the frame dimensions and then do dummy reads |
| captureSave | N/A | Capture frame and save the image file |
| cleanup | N/A | Release the instance's camera connection |
