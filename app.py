#!/usr/bin/env python

import json

from flask import Flask
from flask_socketio import SocketIO

from cofre import Cofre

with open('config.json', 'r') as config_file:
    config = json.loads(config_file)

app = Flask(__name__)
app.secret_key = config['cofre_secret_key']
socketio = SocketIO(app)

socketio.on_namespace(Cofre('/cofre'))

if __name__ == '__main__':
    socketio.run(app, port=8080, debug=True)
