import os, pickle
import cv2 as cv
from keras.models import load_model

# Don't forget add "/" to the end of the path
# data_dir_path = "./sample/"
# tmp = os.listdir(data_dir_path)
# dir_list = sorted([x for x in tmp if os.path.isdir(data_dir_path+x)])

# load label list
dir_list = pickle.load( open("dir_list.pickle", "rb"))

# load learning model
model = load_model('defective_detection_model.h5')

image = cv.imread('test.jpg')
image = cv.resize(image, (100, 100))
image = image.transpose(2,0,1)
image = image/255.
image=image.reshape(1,3,100,100)

dir_label=int(model.predict_classes(image))

print(dir_list[int(dir_label)])

# similarity
pred = model.predict(image)[0]
top = 3
top_indices = pred.argsort()[-top:][::-1]
for i in top_indices:
    print(dir_list[i] + ' : ' + str(round(pred[i]*100,2)) + '%')