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
