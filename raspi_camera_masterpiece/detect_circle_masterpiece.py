import cv2
import requests, threading

class Detect_circle():
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # Don't give a large number to width adn height, it causes delay.
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

    def __del__(self):
        self.video.release()

    def send_image(self, result, filename):
        url = 'http://www.watarunrun.com:5000/masterpiece'
        file = {'media': open('static/' + str(filename), 'rb')}
        res = requests.post(url, files=file, data = {'result':result})
        result = res.text
        print(result)
        return result
