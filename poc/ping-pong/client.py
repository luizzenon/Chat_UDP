#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from __future__ import print_function

from time import sleep
from twisted.internet.protocol import DatagramProtocol, Factory
from twisted.internet import reactor, defer

class EchoClientDatagramProtocol(DatagramProtocol):
    def startProtocol(self):
        self.transport.connect('127.0.0.1', 8000)
        self.transport.write(b"inicio")

    def sendDatagram(self):
        self.transport.write(b"heelp")

    def datagramReceived(self, datagram, host):
        print('Datagram received: ', repr(datagram))
        self.sendDatagram()

def main():
    protocol = EchoClientDatagramProtocol()
    t = reactor.listenUDP(0, protocol)

    try:
        reactor.run()
    except KeyboardInterrupt:
        print("Interrupted by keyboard. Exiting.")
        reactor.stop()

if __name__ == '__main__':
    main()
