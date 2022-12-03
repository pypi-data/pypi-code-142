# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('Requirements.txt') as f:
    Requirements = f.read()

setup(
    name='taichi_q',
    version='0.0.1',
    description='Taichi-Q: A quantum circuit simulator for both CPU and GPU',
    long_description=readme,
    author='Haotian Hong',
    author_email='bughht@outlook.com',
    install_requires=Requirements,
    url='https://github.com/bughht/Taichi-Q',
    license='Apache License Version 2.0',
    packages=find_packages(),
    test_suite='tests'
)
