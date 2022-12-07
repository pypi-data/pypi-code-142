#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/3/29 15:22
# @Author  : xgy
# @Site    : 
# @File    : utils.py
# @Software: PyCharm
# @python version: 3.7.4
"""
import json
import os
import subprocess
import shlex
import ast
import sys
from loguru import logger

import prettytable
from prettytable import PrettyTable
from textwrap import fill


class RunSys:
    """
    执行 shell 命令
    """

    def __init__(self, command: str = None):
        self.command = command
        self.output = None

    def run_cli(self):
        cmd = shlex.split(self.command)
        try:
            # output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            subprocess.check_call(cmd, stderr=subprocess.STDOUT)
            return True
            # self.output = output.decode()
        except subprocess.CalledProcessError as e:
            # print(traceback.print_exc())
            # print(e)
            return False


def format(data, title_dict: dict = None, show=False):
    x = PrettyTable(hrules=prettytable.ALL)
    x.align = "l"

    res_l = data["data"]

    if not title_dict:
        title_dict = {}
        if isinstance(res_l, list):
            for k, v in res_l[0].items():
                title_dict[k] = k
        if isinstance(res_l, dict):
            for k, v in title_dict.items():
                title_dict[k] = k

    # table_data = []
    title = []
    for k, v in title_dict.items():
        title.append(k)
    x.field_names = title

    if res_l:
        if isinstance(res_l, list):
            for item in res_l:
                item_l = []
                for k, v in title_dict.items():
                    if item[title_dict[k]]:
                        item_l.append(fill(str(item[title_dict[k]]), width=20))
                    else:
                        if str(item[title_dict[k]]) == '0' or str(item[title_dict[k]]) == '0.0':
                            # item_l.append(str(item[title_dict[k]]))
                            item_l.append("0")
                        else:
                            item_l.append('')
                x.add_row(item_l)
        if isinstance(res_l, dict):
            item_l = []
            for k, v in title_dict.items():
                if res_l[title_dict[k]]:
                    item_l.append(fill(res_l[title_dict[k]], width=20))
                else:
                    if str(res_l[title_dict[k]]) == '0' or str(res_l[title_dict[k]]) == '0.0':
                        # item_l.append(str(res_l[title_dict[k]]))
                        item_l.append("0")
                    else:
                        item_l.append('')
            x.add_row(item_l)

    if not show:
        print(x)
    return x


def print_error_msg(msg, code):
    result_json = {}
    result_json['error_msg'] = msg
    result_json['error_code'] = code
    # result_json['usage'] = usage
    print(json.dumps(result_json, ensure_ascii=False))


def read_jsonl(jsonl_file):
    try:
        with open(jsonl_file, "r", encoding="utf-8") as fr:
            data = []
            l = fr.readlines()
            for line in l:
                data.append(ast.literal_eval(line))
        return data
    except Exception as ae:
        logger.error("json文件错误", ae)
        sys.exit()


def check_jsonl(folder):
    abs_path = os.path.abspath(folder)
    data_path = None
    file_name = None
    # st_data = None
    for root, _, files in os.walk(abs_path):
        if len(files) != 1:
            raise FileExistsError("数据集结构错误, {} 中文件不止一份".format(abs_path))
        for file in files:
            file_name = file
            data_path = os.path.join(root, file)
            data_path = data_path
    if data_path:
        st_data = read_jsonl(data_path)
        return st_data, file_name


def make_tmp():
    if sys.platform == "win32":
        em_code = "GBK"
    else:
        em_code = "utf-8"

    if sys.platform == "win32":
        tmp_dir = "/tmp"
    elif sys.platform == "linux":
        cmd_user = 'whoami'
        res_login = subprocess.Popen(cmd_user, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        user = res_login.stdout.read().decode("utf-8").rstrip()
        if user == "root":
            tmp_dir = "/tmp"
        else:
            tmp_dir = os.path.join("/home", user, "tmp")
    else:
        raise SystemError("仅支持windows和linux系统")

    return tmp_dir, em_code


if __name__ == '__main__':
    print("start")


