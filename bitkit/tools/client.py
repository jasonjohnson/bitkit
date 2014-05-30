from SocketServer import BaseRequestHandler, TCPServer


class PeerHandler(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        self.request.sendall(data.upper())


def client(address, port, torrent):
    print("Client started: %s:%d" % (address, port))
    print("--")

    server = TCPServer((address, port), PeerHandler)
    server.serve_forever()

