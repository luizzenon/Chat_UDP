from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class BroadcastPingClient(DatagramProtocol):

    def startProtocol(self):
        self.transport.setBroadcastAllowed(True)
        self.transport.write(b'Client: Ping', ("<broadcast>", 9999))

reactor.listenUDP(0, BroadcastPingClient())
reactor.run()
