"""
Always create the flask application object first before importing anything else
to avoid circular imports
"""
from flask import Flask
app = Flask(__name__)
app.debug = True
print "Flask app initialized with name %s" % __name__


import logging
import os
import sys

from flask import request, Response
from socketio import socketio_manage

from config import DevelopmentConfig
from config import ProductionConfig
from socket_server import ChatNamespace


##### set up config
if 'APP_ENV' in os.environ and os.environ['APP_ENV'] == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)


##### import the views so the flask app can route to them
from views import *


##### Setting up logging
log_handler = logging.StreamHandler(sys.stdout)
log_handler = logging.StreamHandler(sys.stdout)
formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

log_handler.setFormatter(formatter)
log_handler.setLevel(logging.DEBUG)

app.logger.addHandler(log_handler)
app.logger.setLevel(logging.DEBUG)


@app.route('/socket.io/<path:remaining>')
def socketio_service(remaining):
    try:
        socketio_manage(request.environ, {'/chat': ChatNamespace}, request)
        app.logger.debug("Socket connection established for chatnamesapce")
    except Exception as e:
        app.logger.error("Exception while handling socketio connection",
                         exc_info=True)
        app.logger.error("  The socketio exception - %s" % e)
    return Response()