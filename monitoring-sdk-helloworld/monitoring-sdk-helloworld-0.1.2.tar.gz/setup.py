#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

from io import open
from setuptools import setup, find_packages

PACKAGE_NAME = "monitoring-sdk-helloworld"

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
with open("CHANGELOG.md", encoding="utf-8") as f:
    changelog = f.read()

install_requires = [
    'requests==2.28.1'
]

setup_requires = [
    "setuptools >= 40.4.3",
    "pip ~= 20.3",
    "wheel",
]

tests_require = [
    "pytest-subtests",
    "pytest-cov",
    "pytest-xdist",
    "numpy",
    "pandas",
    #"pyspark.sql",
]

packages = find_packages(where="src", include=["*"], exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
print("found packages:")
for pkg in packages:
    print("package: %s" % pkg)

setup(
    name=PACKAGE_NAME,
    description="Azure Machine Learning Model Monitoring SDK V2",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/markdown",
    author='Microsoft Corporation',
    author_email='azuremlsdk@microsoft.com',
    license='MIT License',
    keywords=["AzureMachineLearning", "ModelMonitoring"],
    platforms='any',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    packages=packages,
    package_dir={"": "src"},
    test_suite='src.monitoring.src.tests',
    tests_require=tests_require,
    setup_requires=setup_requires,
    extras_require={
        'test': tests_require,
        'setup': setup_requires
    },
    install_requires=install_requires,
)
