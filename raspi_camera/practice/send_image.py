import requests

url = 'http://192.168.2.14:5000/detection'
file = {'media': open('../Cloud/Defective_detection/sample/benign/1581173403_circle.jpg', 'rb')}
res = requests.post(url, files=file)
print(res.text)
