#!/usr/bin/env python3
"""Minimal setup for Grove."""
import os

from setuptools import find_namespace_packages, setup

# setupmeta does not seem to pull in metadata from namespace packages. As a result, we
# need to pull things in ourselves.
__version__ = "0.0.0"
__author__ = "Not Defined"

path = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(path, "grove/__about__.py")).read())  # noqa: S102

# Load the long description for PyPi.
long_description = open(os.path.join(path, "README.md")).read()

setup(
    version=__version__,
    author=__author__,
    packages=find_namespace_packages(include=["grove"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[]
)
