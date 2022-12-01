from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'First'

# Setting up
setup(
    name="susuio",
    version=VERSION,
    author="",
    author_email="<jorbfreire@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'fs'],
    keywords=['python', 'io'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)