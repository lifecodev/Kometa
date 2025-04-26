import json
import os

from flask import render_template, Response
from app import app

@app.route("/api")
def api_info():
    data = {
        'version':os.environ.get('API_VERSION')
    }
    resp = Response(json.dumps(data))
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route("/api/users/<user_id>", methods=['GET'])
def users_get(user_id: int):

    # TODO: проверка jwt токена или Oauth (на выбор)
    return str(user_id)
    pass

@app.route("/api/users/<user_id>", methods=['PUT'])
def users_put(user_id: int):
    # TODO: проверка jwt токена или Oauth (на выбор)
    return str(user_id)
    pass


