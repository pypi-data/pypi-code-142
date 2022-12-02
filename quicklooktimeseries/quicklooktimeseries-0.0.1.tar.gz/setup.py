from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'quicklook time series data'

# Setting up
setup(
    name="quicklooktimeseries",
    version=VERSION,
    author="Hong Tang",
    author_email="<stanghong@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['python', 'pandas'],
    keywords=['python', 'timeseries','plot'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
