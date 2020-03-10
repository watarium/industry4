# import the necessary packages
import numpy as np
import cv2
import datetime, time, requests, threading
from OPC_client import switch

class Detect_circle(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # Don't give a large number to width adn height, it causes delay.
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

    def __del__(self):
        self.video.release()

    def send_image(self):
        url = 'http://www.watarunrun.com:5000/detection'
        file = {'media': open('./extracted_image.jpg', 'rb')}
        res = requests.post(url, files=file)
        result = res.text
        print(result)

        # In the future, I'll use another Raspberry Pi as PLC
        switch(result.split()[0])

        return result

    def circle_finder(self):
        success, image = self.video.read()
        output = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect circles in the image
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=2, minDist=500, param1=100, param2=100)
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(image, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

            # Execute every 5 seconds
            sec = datetime.datetime.now().second
            if sec % 5 == 0:
                # Extract the circle
                x = circles[0][0]
                y = circles[0][1]
                r = circles[0][2]
                extracted_image = output[y - r:y + r, x - r:x + r]
                cv2.imwrite('./extracted_image.jpg', extracted_image)
                time.sleep(1)
                thread = threading.Thread(target=self.send_image)
                thread.start()


        # Convert to bytes type using.tobytes() because cv2.imencode() returns numpy.ndarray().
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
