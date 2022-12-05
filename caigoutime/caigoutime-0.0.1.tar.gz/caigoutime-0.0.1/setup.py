#!/usr/bin/python3
#Author:代钰
# -*- coding: utf-8 -*-
# @Time    : 2022/12/5 20:35
# @Author  : Mat
# @Site   : 
# @File    : setup.py.py
# @Software: PyCharm


from setuptools import setup, find_packages
setup(
name="caigoutime",
version="0.0.1",
author="daiyu",
author_email="2574451281@qq.com",
description="This project is to make viewing time more convenient",
# 项目主页
# url="https://github.com/sunjian-github/ezface",
# 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
packages=find_packages()
)