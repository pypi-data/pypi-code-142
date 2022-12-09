#!/usr/bin/env python3
import requests

def is_in_china()->bool:
    """decide if the machine is in china"""
    ipinfo = requests.get('http://ipinfo.io/json').json()
    return ipinfo['country'] == 'CN'

        