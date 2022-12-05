from setuptools import setup, find_packages
# from distutils.core import setup
import codecs
import os


VERSION = '0.0.3'
DESCRIPTION = 'addup'

# Setting up
setup(
    name="addup",
    version=VERSION,
    author="Hong Tang",
    author_email="<stanghong@gmail.com>",
    description=DESCRIPTION,
    # url = 'https://github.com/stanghong/pypi_publication', 
    # packages=find_packages('addup'),
    packages=['libname'],
    install_requires=['numpy','pandas',],
    # download_url = 'https://github.com/stanghong/pypi_publication/archive/refs/tags/v0.0.9.tar.gz',
    
    keywords=['python', 'test','plot'],

    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
