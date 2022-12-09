# -*- coding:utf-8 -*-

import os
import subprocess


def stop_winmail_service():
    """
    停止Winmail服务
    """
    if os.name == "nt":
        subprocess.call("net stop magicwinmailserver", shell=True)
    if os.name == "posix":
        subprocess.call("systemctl stop winmail", shell=True)


def start_winmail_service():
    """
    启动Winmail服务
    """
    if os.name == "nt":
        subprocess.call("net start magicwinmailserver", shell=True)
    if os.name == "posix":
        subprocess.call("systemctl start winmail", shell=True)