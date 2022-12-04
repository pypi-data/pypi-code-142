#!/usr/bin/env python

from setuptools import setup
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")
install_requires = []

setup(
    name="keywordlist",
    version="1.0.0",
    description="Keyword Wordlist Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tibotix",
    author_email="tizian@seehaus.net",
    url="https://github.com/tibotix/keywordlist",
    package_dir={"keywordlist": "src"},
    packages=["keywordlist"],
    install_requires=install_requires,
    extras_require={"test": ["pytest"]},
    python_requires=">=3.8, <4",
)