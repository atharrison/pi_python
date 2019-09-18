import os
import socket
import subprocess


class IPAddress:

    def __init__(self):
        if os.name == 'nt':
            self.on_windows = True
        else:
            self.on_windows = False

    def ip(self):
        if self.on_windows:
            return socket.gethostbyname(socket.gethostname())
        else:
            return subprocess.check_output(['hostname', '-I']).decode("utf-8").split(" ")[0]
