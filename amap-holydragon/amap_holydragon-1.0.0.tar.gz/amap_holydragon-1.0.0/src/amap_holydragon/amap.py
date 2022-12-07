# coding:utf-8
"""
amap

Usage:
  amap <ip_address_or_domain_name> [options]

Options:
  -h --help  Show help information
  -n --nmap  Use nmap tool to scan

"""

from docopt import docopt
import socket
import subprocess
import json


def amap():
    arguments = docopt(__doc__)

    target = arguments['<ip_address_or_domain_name>']
    try:
        socket.getaddrinfo(target, None)
    except:
        print('Invalid IP address or domain name!')
        exit(1)

    if arguments['--nmap']:
        result = subprocess.run(["nmap", target], capture_output=True, text=True).stdout
    else:
        result = json.loads(
            subprocess.run(["curl", "http://amap.fofa.info/" + target], capture_output=True, text=True).stdout)
        # Timeout
        i = 0
        while 'error' in result and i < 2:
            result = json.loads(
                subprocess.run(["curl", "http://amap.fofa.info/" + target], capture_output=True, text=True).stdout)
            i = i + 1
    print(result)
