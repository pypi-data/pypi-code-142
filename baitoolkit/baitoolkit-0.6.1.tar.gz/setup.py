# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages


"""
baiToolkit
----------------
Core tools for your web & AI application
"""


def load_requirements():
    with open('requirements.txt') as f:
        packages = f.read().strip().split('\n')
        return [pkg for pkg in packages]


def read_description():
    with open('README.md') as f:
        return f.read()


setup(
    name="baitoolkit",
    description="Core development tools for web & AI application.",
    long_description=read_description(),
    keywords="Web, Database, Flask, Click, SQLAlchemy, Migration, Config",
    packages=find_packages(exclude=['data', 'tests']),
    install_requires=load_requirements()
)
