#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Created Time:  2018-1-23 19:17:34

# https://blog.51cto.com/u_13760719/5677395
#############################################


from setuptools import setup, find_packages

setup(
    name = "magetool_zhengfeng2",
    version = "0.1.4",
    keywords = ("pip", "pathtool","timetool", "magetool_zhengfeng", "mage"),
    description = "time and path tool",
    long_description = "time and path tool",
    license = "MIT Licence",

    url = "https://github.com/fengmm521/pipProject",
    author = "zhengfeng",
    author_email = "mage@woodcol.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)