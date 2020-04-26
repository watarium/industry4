import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route('/masterpiece', methods=['POST'])
def masterpiece():
    file = request.files['media']
    print(request.form['result'])
    result = request.form['result']

    now = datetime.datetime.now()
    filename = "{0:%Y%m%d-%H%M%S}.jpg".format(now)

    if result == 'benign':
        file.save('./benign/' + filename)
        print('Data was saved into benign folder as ' + str(filename))
    if result == 'defective':
        file.save('./defective/' + filename)
        print('Data was saved into defective folder as ' + str(filename))
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0')


