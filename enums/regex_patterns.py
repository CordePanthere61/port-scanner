from enum import Enum


class RegexPatterns(Enum):
    IP = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    HOSTNAME = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zAZ0-9])?\.)+[a-zA-Z]{2,}$"
    PORTS = r'^-p((\d+-\d+)|(\d+(,\d+)*))$'
