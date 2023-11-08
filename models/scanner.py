import socket
from threading import Thread, Lock
from models.target import Target
from utils.banner_grabber import BannerGrabber


class Scanner:
    target: Target
    open_ports: [int]
    open_ports_lock: Lock

    def scan(self, target) -> 'Scanner':
        self.target = target
        self.open_ports = []
        self.open_ports_lock = Lock()
        threads = []
        for port in self.target.ports:
            thread = Thread(target=self.connect_to_port, args=[self.target.host, port])
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
        return self

    def connect_to_port(self, host: str, port: int):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1)

            client.connect((host, port))

            print(BannerGrabber().grab(host, port, client))

            self.open_ports_lock.acquire()
            self.open_ports.append(port)
            self.open_ports_lock.release()
            client.close()
        except socket.error:
            return

    def print_result(self):
        self.open_ports.sort()
        for port in self.open_ports:
            print(f"{port} | OPEN | {socket.getservbyport(port)}")
