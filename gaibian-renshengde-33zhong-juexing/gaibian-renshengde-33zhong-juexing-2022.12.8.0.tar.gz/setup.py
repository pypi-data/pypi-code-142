#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import GaibianRenshengde33zhongJuexing
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('GaibianRenshengde33zhongJuexing'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="gaibian-renshengde-33zhong-juexing",
    version=GaibianRenshengde33zhongJuexing.__version__,
    url="https://github.com/apachecn/gaibian-renshengde-33zhong-juexing",
    author=GaibianRenshengde33zhongJuexing.__author__,
    author_email=GaibianRenshengde33zhongJuexing.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="改变人生的33种觉醒 ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "gaibian-renshengde-33zhong-juexing=GaibianRenshengde33zhongJuexing.__main__:main",
            "GaibianRenshengde33zhongJuexing=GaibianRenshengde33zhongJuexing.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
