from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.1.0'
DESCRIPTION = 'A simple JSON string creator that takes whatever you have and transform it into a String'

with open("jsonwhatever/README.MD", "r",encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
    name='jsonwhatever',
    version=VERSION,
    author='dazjuancarlos',
    author_email='dazjuancarlos@gmail.com',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    license='MIT',
    keywords=['python','json','simple'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)