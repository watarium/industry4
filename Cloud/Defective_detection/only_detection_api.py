import pickle
import numpy as np
import cv2 as cv
from keras.models import load_model
from flask import Flask, request
import tensorflow as tf

# load label list
dir_list = pickle.load(open("dir_list.pickle", "rb"))
# save learning model
model = load_model('defective_detection_model.h5')
graph = tf.get_default_graph()

app = Flask(__name__)

@app.route('/detection', methods=['POST'])
def detection():
    global graph
    with graph.as_default():
        stream = request.files['media'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        image = cv.imdecode(img_array, 1)
        image = cv.resize(image, (100, 100))
        image = image.transpose(2, 0, 1)
        image = image / 255.
        image = image.reshape(1, 3, 100, 100)

        dir_label = int(model.predict_classes(image))

        # similarity
        pred = model.predict(image)[0]
        top = 1
        top_indices = pred.argsort()[-top:][::-1]
        for i in top_indices:
            print(dir_list[i] + ' : ' + str(round(pred[i] * 100, 2)) + '%')
            result = dir_list[i] + ' : ' + str(round(pred[i] * 100, 2)) + '%'

        return result

if __name__ == '__main__':
    app.run(host='0.0.0.0')
