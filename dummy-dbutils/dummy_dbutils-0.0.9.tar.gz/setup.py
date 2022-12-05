from setuptools import setup, find_packages
import os

VERSION = '0.0.9'
DESCRIPTION = 'Dummy Scripts for Databricks dbutils'
LONG_DESCRIPTION = 'A package that allows to use databricks dbutils without actual functionality. This helps to generate the build.'

# Setting up
setup(
    name="dummy_dbutils",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),

    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)