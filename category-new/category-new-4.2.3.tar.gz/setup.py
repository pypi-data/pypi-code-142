from setuptools import setup, find_packages
import codecs
import os

VERSION = '4.2.3'
DESCRIPTION = 'A basic hello package'
#LONG_DESCRIPTION = 'A basic hello package, used for research purposes'

# Setting up
setup(
    name="category-new",
    version=VERSION,
    author="Studena123 (Jana Vojnovic)",
    author_email="<janavojno00@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    #long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'helloworld'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)