from flask import Blueprint, request, jsonify
from ml import Model


sp_monkey = Blueprint('monkey', __name__)

@sp_monkey.route('/ml', methods=['POST'])
def teste():
    logicals  = request.json['logicals']
    model = Model()
    model.train()
    n  = model.predict(logicals)
    return  jsonify({ 'data' : str(n) })
@sp_monkey.route('/args', methods=['GET'])
def page():
    x = request.args['x']
    y = request.args['y']
    model = Model()
    model.train()
    n  = model.predict([int(x),int(y)])
    return jsonify({ 'data' : str(n)})