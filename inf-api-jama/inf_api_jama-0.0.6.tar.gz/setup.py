from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.0.6'
DESCRIPTION = 'Jama API'
LONG_DESCRIPTION = 'A package that allows to create TCs for every ReQ automatically and more.'

# Setting up
setup(
    name="inf_api_jama",
    version=VERSION,
    author="Raphael Trinkler",
    author_email="<raphael.trinkler@infineon.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[ "pynput", "requests", "requests_ntlm" ],
    keywords=['python', "Jama"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)