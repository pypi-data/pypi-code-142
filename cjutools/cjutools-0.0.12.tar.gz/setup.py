#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: cjylzs(691086891@qq.com)
# Description: tools depend cjutils

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    setup(
        name='cjutools',
        version='0.0.12',
        keywords='cjutools',
        description='tools depend cjutils',
        long_description=f.read(),
        license='MIT License',
        url='https://github.com/CJYLZS/cjtools.git',
        author='cjylzs',
        author_email='691086891@qq.com',
        packages=find_packages(),
        include_package_data=True,
        platforms='any',
        install_requires=['cjutils>=0.0.25']
    )
