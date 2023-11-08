from utils.arguments_parser import ArgumentsParser


class Target:
    host: str
    ports: [int]

    def __init__(self, argv: [str]):
        argument_parser = ArgumentsParser(argv)
        self.host = argument_parser.format_target_host()
        self.ports = argument_parser.format_target_ports()
