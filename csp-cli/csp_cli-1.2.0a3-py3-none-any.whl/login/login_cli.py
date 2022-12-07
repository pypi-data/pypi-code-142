#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/11/16 16:42
# @Author  : xgy
# @Site    : 
# @File    : login_cli.py
# @Software: PyCharm
# @python version: 3.7.13
"""

import click
from csp.command.cli import csptools


# 一级命令 csp login
@csptools.command()
@click.option("-u", "--username", prompt="用户名", help="用户名", required=True)
# @click.option("-p", "--passwd", prompt="密码", help="密码", required=True, hide_input=True, confirmation_prompt=True)
@click.option("-p", "--passwd", prompt="密码", help="密码", required=True, hide_input=True)
def login(username, passwd):
    """
    用户登录命令

    \b
    使用示例：csp login -u "用户名" -p "用户密码"
    """
    try:
        from csp.login.login_server import user_login
        user_login(username, passwd)
        print("登录成功")
    except KeyError as ke:
        print("KeyError: ", str(ke))
    except Exception as ae:
        print(str(ae))


# 一级命令 csp logout
@csptools.command()
def logout():
    """
    用户退出登录命令

    \b
    使用示例：csp logout
    """
    try:
        from csp.login.login_server import user_logout
        user_logout()
    except KeyError as ke:
        print("KeyError: ", str(ke))
    except Exception as ae:
        print(str(ae))


if __name__ == '__main__':
    print("start")
