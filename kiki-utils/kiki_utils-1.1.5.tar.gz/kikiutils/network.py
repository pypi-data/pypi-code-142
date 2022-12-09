import socket
import urllib3


# Network utils

def get_domain_ip(domain: str):
    return socket.gethostbyname(domain)


def get_host(url: str, get_raw_data: bool = False):
    """Get the host of the input url."""

    host = urllib3.get_host(url)
    return host if get_raw_data else host[1]


def domains_is_ip(domains: list[str], ip: str):
    return all([get_domain_ip(domain) == ip for domain in domains])


def int_ip2ip(int_ip: str):
    """Convert int ip to string."""

    if isinstance(int_ip, str):
        return int_ip

    ip = []

    for _ in range(4):
        ip.append(str(int_ip & 255))
        int_ip >>= 8

    return '.'.join(ip[::-1])


def ip2int_ip(ip: str):
    """Convert string ip to int."""

    if isinstance(ip, int):
        return ip

    int_ip = 0

    for i in ip.split('.'):
        int_ip = int_ip << 8 | int(i)

    return int_ip
