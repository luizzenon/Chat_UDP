from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class PingClient(DatagramProtocol):

    def startProtocol(self):
        self.transport.write(b'Client: Ping', (127.0.0.1, 9999))

reactor.listenUDP(0, PingClient())
reactor.run()
