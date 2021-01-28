import cv2

### Device IDs ###
DeviceIdArr = [0, 1, 2, 3, 4, 5]

### Number of Cameras ###
numDevice = len(DeviceIdArr)

### Attributes and Methods for Individual Cameras ###
class Camera:
    def __init__(self, cameraId):
        self.cameraId = cameraId

    def captureSave:
        # Open the device at the designated ID
        cap = cv2.VideoCapture(self.cameraId)

        if not(cap.isOpened()):
            # Check whether the selected camera is opened successfully
            raise Exception("Could not open the device. ID: {}".format(self.cameraId))
        else:
            # Set the resolution
            cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
            # capture the frame
            ret, frame = cap.read()
            # save the frame
            cv2.imwrite("ID{}.jpg", frame)
            # release the camera
            cap.release()

### Create the required number of Camera instances ###
camerasList = list()
for Id in DeviceIdArr:
    cameras.append(Camera(Id))

### For each instance, capture and save each frame ###
for camera in cameraList:
    camera.captureSave()
