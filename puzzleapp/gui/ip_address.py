import socket


class IPAddress:

    def __init__(self):
        hostname = socket.gethostname()
        self.address = socket.gethostbyname(hostname)

    def ip(self):
        return self.address
