import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PySimpleInput",
    version = "0.0.3",
    author = "Turtleion",
    author_email = "remastred89@gmail.com",
    description = ("Package that help you to fix general python input() problems"),
    license = "MIT",
    keywords = "Simple ways to use Input",
    url = "https://github.com/turtleion/PySimpleInput",
    packages=['PySimpleInput'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
