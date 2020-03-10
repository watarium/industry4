import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(1)

    for i in range(100):
        now = str(time.time()).split('.')[0]
        camera.capture('/var/tmp/photos/' + now + '.jpg')