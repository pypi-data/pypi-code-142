import uuid
import socket


def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac

def get_hostName():
    hostname = socket.gethostname()  # 获取本机IP
    return hostname

def get_hostip():
    ip = socket.gethostbyname(get_hostName())
    return ip


