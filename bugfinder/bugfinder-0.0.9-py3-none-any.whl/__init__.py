#!/usr/bin/env python3
from typing import Dict, List, Optional, Set, Tuple

import sys
import os
from bugfinder.utils import is_in_china
import codefast as cf


def dbinstall():
    """install database"""
    is_cn = is_in_china()
    pypi = "https://pypi.douban.com/simple" if is_cn else "https://pypi.org/simple"
    cmd = 'python3 -m pip install {} -i {}'.format(' '.join(sys.argv[1:]), pypi)
    os.system(cmd)


def syncfile():
    file = sys.argv[1]
    try:
        cmd = f"curl -s https://file.ddot.cc/gofil|bash -s {file}"
        resp = os.system(cmd)
        print(resp)
    except FileNotFoundError as e:
        print(e)


def esyncfile():
    """sync file with encryption"""
    file = sys.argv[1]
    try:
        cmd = f"curl -s https://file.ddot.cc/gofile|bash -s {file}"
        resp = os.system(cmd)
        print(resp)
    except FileNotFoundError as e:
        print(e)


def osssync():
    """sync file with encryption"""
    file = sys.argv[1]
    try:
        cmd = f"curl -s https://host.ddot.cc/oss|bash -s {file}"
        resp = os.system(cmd)
        print(resp)
    except FileNotFoundError as e:
        print(e)


def justdemo():
    print("just demo")

def qgrep():
    cf.shell('grep {} /log/serving/serving.log'.format(' '.join(sys.argv[1:])))

from bugfinder.asrsummary import save_record, calculate_summary

exported = ['dbinstall', 'syncfile', 'esyncfile', 'osssync', 'save_record', 'calculate_summary', 'qgrep']
