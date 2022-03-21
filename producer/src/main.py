from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/first', methods=['GET'])
def first():
    ids = [*range(1, 10), *range(31, 40)]
    data = []
    for id_ in ids:
        data.append({'name': f'Test {id_}', 'id': id_, 'file': 'first'})
    return jsonify(data)


@app.route('/second', methods=['GET'])
def second():
    ids = [*range(11, 20), *range(41, 50)]
    data = []
    for id_ in ids:
        data.append({'name': f'Test {id_}', 'id': id_, 'file': 'second'})
    return jsonify(data)


@app.route('/third', methods=['GET'])
def third():
    ids = [*range(21, 30), *range(51, 60)]
    data = []
    for id_ in ids:
        data.append({'name': f'Test {id_}', 'id': id_, 'file': 'third'})
    return jsonify(data)
