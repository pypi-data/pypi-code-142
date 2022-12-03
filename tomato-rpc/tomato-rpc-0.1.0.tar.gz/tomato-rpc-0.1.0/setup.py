#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time : 2022/12/3 10:40 PM
# @author : LiShiChao
import setuptools

with open("READMD.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='tomato-rpc',  # 模块名称
    version="0.1.0",  # 当前版本
    author="LiShiChao",  # 作者
    author_email="lishichao1181@163.com",  # 作者邮箱
    description="基于asyncio+redis实现rpc",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    url="https://github.com/lishichao1181/aio-redis-rpc",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    # install_requires=[],
    python_requires='>=3.6',
)
