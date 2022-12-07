from io import open
from setuptools import setup


"""
: authors: Peopl3s
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2021 Peop13s
"""

version = '1.0'

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="LAVAPI",
    version=version,
    author="DIMFLIX",
    author_email="dimflix.official@gmail.ru",
    description=(
        u'The LAVAPI library was created in order to facilitate work with the official API of the LAVA payment system.'
        u'It presents all the methods present in the official documentation.'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DIMFLIX-OFFICIAL/LAVAPI",
    download_url="https://github.com//DIMFLIX-OFFICIAL/LAVAPI/archive/refs/heads/main.zip",
    license="MIT License",
    packages=['LAVAPI'],
    install_requires=['requests'],
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython"
    ]


)
