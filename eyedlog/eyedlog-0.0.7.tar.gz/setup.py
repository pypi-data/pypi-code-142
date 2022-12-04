# -*- coding: utf-8 -*-

import ast
import re
from setuptools import setup, find_packages


def get_version():
    with open('eyedlog/__version__.py', 'rb') as fh:
        version = re.search(r'__version__\s+=\s+(.*)', fh.read().decode('utf-8')).group(1)
        return str(ast.literal_eval(version))


def get_long_desc():
    with open('README.md', 'r') as fh:
        return fh.read()


setup(
    name='eyedlog',
    version=get_version(),
    author='Ferras Meng',
    author_email='469611602@qq.com',
    description='Colored log',
    long_description=get_long_desc(),
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://gitee.com/ferras/eyedlog',
    install_requires=[],
    setup_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['colored', 'readable', 'log'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
