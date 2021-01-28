import cv2

### Device IDs ###
deviceIdArr = [0, 2, 4]

### Attributes and Methods for Individual Cameras ###
class Camera:
    def __init__(self, cameraId):
        self.cameraId = cameraId
        self.dummyCount = 5
        self.tryCount = 5

    def setup(self):
        # open the device at the designated ID and leave it open
        self.cap = cv2.VideoCapture(self.cameraId)
        if not(self.cap.isOpened()):
            print("Could not open the device. Device ID: {}".format(self.cameraId))

        # set frame dimensions
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 45)

        # dummy read
        for i in range(self.dummyCount):
            dummyRet, dummyFrame = self.cap.read()

    def captureSave(self):
        while(self.tryCount != 0):
            ret, frame = self.cap.read()
            if not(ret):
                # in case read() failed
                self.tryCount -= 1
                print("Failed to grab frame. Try: {} Device ID: {}".format(
                    self.tryCount, self.cameraId))
            else:
                # save image
                cv2.imwrite("ID{}.jpg".format(self.cameraId), frame)
                self.tryCount = 0

    def cleanup(self):
        # release and delete
        self.cap.release()
        del(self.cap)


### Create the required number of Camera instances ###
camerasList = list()
for Id in deviceIdArr:
    camerasList.append(Camera(Id))

### Initialize all camera instances ###
for camera in camerasList:
    camera.setup()

### For each instance, capture and save each frame ###
for camera in camerasList:
    camera.captureSave()

### Release and delete all cameras ###
for camera in camerasList:
    camera.cleanup()
