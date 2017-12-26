#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


import time

while True:
    time.sleep(30)

    class EchoClientDatagramProtocol(DatagramProtocol):
        strings = [
            b"Ping",
        ]

        def startProtocol(self):
            self.transport.connect('127.0.0.1', 9999)
            self.sendDatagram()

        def sendDatagram(self):
            if len(self.strings):
                datagram = self.strings.pop(0)
                self.transport.write(datagram)
                print("entrou")

            else:
                print("else")
                reactor.stop()

        def datagramReceived(self, datagram, host):
            print(type(datagram))
            print('Datagram received: ', repr(datagram))
            self.sendDatagram()

    def main():
        protocol = EchoClientDatagramProtocol()
        t = reactor.listenUDP(0, protocol)
        try:
            reactor.run()
        except:
            print("erroooo")
            pass
    if __name__ == '__main__':
        main()
