from gevent import monkey
monkey.patch_all()

from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

from application import app


class ChatNamespace(BaseNamespace, BroadcastMixin):

    def on_clientmessage(self, msg):
        app.logger.debug("ChatNamespace  - Received on clientmessage - %s" % msg)
        self.broadcast_event('servermessage', msg + "----" + msg);
        # self.emit('servermessage', msg + "----" + msg)
