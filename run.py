#!/usr/bin/env python

from flask import Flask
from flask_socketio import SocketIO

from cofre.models import Cofre
import config

app = Flask(__name__)
app.secret_key = config.APP_SECRET_KEY
socketio = SocketIO(app)

socketio.on_namespace(Cofre('/cofre'))

if __name__ == '__main__':
    socketio.run(app, port=config.PORT, debug=config.DEBUG)
