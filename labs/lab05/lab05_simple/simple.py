from json import dumps
from flask import Flask, request

app = Flask(__name__)

names = []

@app.route('/name/add', methods=['POST'])
def name_add():
    global names
    data = request.get_json()
    names.append(data['name'])
    return dumps({})


@app.route('/name/get', methods=['GET'])
def name_get():
    return dumps({'names': names})


@app.route('/name/remove', methods=['DELETE'])
def name_remove():
    global names
    data = request.get_json()
    names.remove(data['name'])
    return dumps({})


if __name__ == "__main__":
    app.run(port=0)