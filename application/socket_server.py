from gevent import monkey
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

monkey.patch_all()


class ChatNamespace(BaseNamespace, BroadcastMixin):

    def on_clientmessage(self, msg):
        print "ChatNamespace  - Received on clientmessage - %s" % msg
        self.broadcast_event('servermessage', msg + "----" + msg);
        # self.emit('servermessage', msg + "----" + msg)
