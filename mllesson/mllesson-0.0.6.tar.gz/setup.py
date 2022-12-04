#!/usr/bin/env python
# -*- coding:utf8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mllesson",
    version="0.0.6",
    author="wolido",
    author_email="270262953@qq.com",
    description="机器学习课程辅助",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",#使用Python3
        "License :: OSI Approved :: Apache Software License",#开源协议
        "Operating System :: OS Independent",
    ],
)
