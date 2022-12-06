#!/usr/bin/env python

from distutils.core import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="Article Analyzer",
    version="0.1",
    description="Learn from trainingsdata a classifier to label article",
    author="Jan Bernoth",
    author_email="jan.bernoth@uni-potsdam.de",
    license="MIT",
    long_description=long_description,
    py_modules=['artan']
)