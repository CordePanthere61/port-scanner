from socket import socket
from typing import Dict, Callable


def ssh_banner(host: str, client: socket) -> str:
    return client.recv(4096).decode()


def http_banner(host, client: socket) -> str:
    print("HERE")
    client.send(b"GET / HTTP/1.1\r\nHost: " + host + b"\r\n\r\n")
    return client.recv(4096).decode()


class BannerGrabber:
    port_to_function: Dict[int, Callable[[str, socket], str]]

    def __init__(self):
        self.port_to_function = {
            22: ssh_banner,
            80: http_banner
        }

    def grab(self, host: str, port: int, client: socket) -> str:
        function = self.port_to_function.get(port)
        try:
            return function(host, client)
        except TypeError:
            return ""
