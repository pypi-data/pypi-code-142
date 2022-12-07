#! usr/bin/python
# -*- coding: utf-8 *-*

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='restutil',
    packages=['restutil'],
    version='1.0',
    description='Rest Util Tools',
    author='Adonis González',
    author_email='adions025@gmail.com',
    url='https://github.com/adions025/restutil',
    download_url='https://github.com/adions025/restutil',
    keywords=['Restful', 'Rest', 'Util', 'Tools'],
    long_description="""This is Tool implementation"""
)
