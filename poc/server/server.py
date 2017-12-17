import logging
import argparse
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

logger = logging.getLogger('myapp')


class Echo(DatagramProtocol):
    def datagramReceived(self, data, host_port):
        (host, port) = host_port
        logger.info("received {} from {}:{}".format(data, host, port))
        self.transport.write(data, (host, port))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-n', '--node-name', required=True)

    args = parser.parse_args()

    hdlr = logging.FileHandler('{}.log'.format(args.node_name))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

    reactor.listenUDP(9999, Echo())
    reactor.run()
