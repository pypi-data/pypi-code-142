#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
from _version import __version__

setup(
    name='testpublishzhangxin',
    version=__version__,
    description=(
        'a test'
    ),
    long_description=open('README.md').read(),
    author='zhangxin',
    author_email='394845773@qq.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url = "https://github.com/sola7693/test_github_action",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries'
    ]
)