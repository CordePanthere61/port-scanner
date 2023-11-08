import sys
import re
from typing import Dict

from enums.regex_patterns import RegexPatterns

HOST_KEY = "host"
PORTS_KEY = "ports"


class ArgumentsParser:
    raw_args_array: [str]
    args: Dict[str, str] = {}

    def __init__(self, args: [str]):
        self.raw_args_array = args
        self.parse_arguments()

    def parse_arguments(self):
        for i in range(1, len(self.raw_args_array)):
            self._extract_raw_host(self.raw_args_array[i])
            self._extract_raw_ports(self.raw_args_array[i])

    def _extract_raw_host(self, arg: str) -> None:
        ip_match = re.match(RegexPatterns.IP.value, arg)
        host_match = re.match(RegexPatterns.HOSTNAME.value, arg)
        if not ip_match and not host_match:
            return
        elif HOST_KEY in self.args:
            sys.exit("Cannot have multiple ip addresses")
        else:
            self.args[HOST_KEY] = arg

    def _extract_raw_ports(self, arg: str) -> [int]:
        match = re.match(RegexPatterns.PORTS.value, arg)
        if not arg.startswith("-p"):
            return
        elif not match:
            sys.exit("Invalid port(s) option")
        elif PORTS_KEY in self.args:
            sys.exit("Cannot have multiple port(s) options")
        else:
            self.args[PORTS_KEY] = arg.replace("-p", "")

    def format_target_ports(self) -> [int]:
        if PORTS_KEY not in self.args:
            return list(range(1, 1025))
        elif ',' in self.args[PORTS_KEY]:
            return [int(num) for num in self.args[PORTS_KEY].split(',')]
        elif '-' in self.args[PORTS_KEY]:
            start, end = map(int, self.args[PORTS_KEY].split('-'))
            return list(range(start, end + 1))
        else:
            return [int(self.args[PORTS_KEY])]

    def format_target_host(self) -> str:
        if HOST_KEY not in self.args:
            sys.exit("Must specify a hostname or IP address")
        else:
            return self.args[HOST_KEY]

