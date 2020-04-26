from flask import *
from detect_circle_masterpiece import Detect_circle
import picamera, time, datetime
from OPC_client import switch

Detect_circle = Detect_circle()

def take_picture(filename):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('static/' + str(filename))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', img_url='static/' + str(filename))

@app.route('/benign', methods=['POST'])
def benign():
    global filename
    switch('benign')
    result = 'benign'
    Detect_circle.send_image(result, filename)
    now = datetime.datetime.now()
    filename = "{0:%Y%m%d-%H%M%S}.jpg".format(now)
    take_picture(filename)
    return render_template('index.html', img_url='static/' + str(filename))

@app.route('/defective', methods=['POST'])
def defective():
    global filename
    switch('defective')
    result = 'defective'
    Detect_circle.send_image(result, filename)
    now = datetime.datetime.now()
    filename = "{0:%Y%m%d-%H%M%S}.jpg".format(now)
    take_picture(filename)
    return render_template('index.html', img_url='static/' + str(filename))

if __name__ == '__main__':
    now = datetime.datetime.now()
    filename = "{0:%Y%m%d-%H%M%S}.jpg".format(now)
    take_picture(filename)
    app.run(host='0.0.0.0', threaded=True)
