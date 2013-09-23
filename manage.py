from flask.ext.script import Manager
from gevent import monkey
from socketio.server import SocketIOServer

from application import app

monkey.patch_all()
manager = Manager(app)


@manager.command
def hello():
    print "Whatever!!"


@manager.command
def runserver():
    """
    Look into the following if socket server does not stop
    http://stackoverflow.com/questions/15932298/how-to-stop-a-flask-server-running-gevent-socketio
    """
    app.logger.debug("Trying to run server")
    socket_server = SocketIOServer(('', 5000), app, resource="socket.io",
                                   policy_server=False)
    socket_server.serve_forever()
    app.logger.debug("Successfully created a socket server over a flask app")

    # Definetely need to have this commented, running both socketserver and
    # flask causes error
    # app.run()

if __name__ == '__main__':
    manager.run()
