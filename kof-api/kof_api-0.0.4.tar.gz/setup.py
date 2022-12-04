from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.4'
DESCRIPTION = 'API for Kingdoms of Fortune.'

# Setting up
setup(
    name="kof_api",
    version=VERSION,
    author="GalaxyIndieDev",
    author_email="<zachnichelson304@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'api', 'kof', 'video game'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)