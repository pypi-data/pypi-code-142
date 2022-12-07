"""
    快捷启动方式，便于调试
"""
import os
import sys
from mitmproxy.tools.main import mitmdump

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def execute(filepath: str, port: int = 8866):
    """

    :param filepath: 启动文件路径
    :param port: 端口
    :return:
    """
    mitmdump(['-p', str(port), '-s', filepath])
