import os

from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def read(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        next(data)
        for line in data:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))
    return [x, y]


@app.route('/test', methods=['GET'])
def test():
    data = read('airfoils/0006.dat')
    return jsonify(data)


@app.route('/airfoils', methods=['GET'])
def airfoils():
    airfoil_folder = r'airfoils'
    airfoil_files = os.listdir(airfoil_folder)
    airfoil_choices = [x[:-4] for x in airfoil_files]
    return jsonify(airfoil_choices)


@app.route('/airfoil', methods=['GET'])
def get_airfoil():
    airfoil = request.args.get('airfoil')
    data = read('airfoils/' + str(airfoil) + '.dat')
    return jsonify(data)

if __name__ == '__main__':
    app.run()
