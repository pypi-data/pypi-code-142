#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

setuptools.setup(
    name="battleship-py",
    version="0.2.0",
    author="João Magalhães",
    author_email="joamag@gmail.com",
    description="Simple Battleship game",
    license="Apache License, Version 2.0",
    keywords="game battleship",
    url="http://joao.me",
    zip_safe=False,
    packages=["battleship", "battleship.test"],
    test_suite="battleship.test",
    package_dir={"": os.path.normpath("src")},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md"), "rb")
    .read()
    .decode("utf-8"),
    long_description_content_type="text/markdown",
)
