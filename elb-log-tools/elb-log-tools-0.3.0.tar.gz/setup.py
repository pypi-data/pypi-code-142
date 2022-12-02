#!/usr/bin/env python3
import os
from typing import Dict

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
src = os.path.join(here, "elb_log_tools")


with open("README.md", "r") as f:
    readme = f.read()

about: Dict[str, str] = {}
with open(os.path.join(src, "__version__.py")) as f:
    exec(f.read(), about)


setup(
    name="elb-log-tools",
    version=about["__version__"],
    description="Tools for processing logs from AWS Elastic Load Balancer",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Pymetrics, Inc.",
    author_email="info@pymetrics.com",
    url="https://github.com/pymetrics/elb-log-tools",
    install_requires=["boto3"],
    tests_require=["pytest"],
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: Log Analysis",
    ],
    packages=["elb_log_tools"],
    entry_points={
        "console_scripts": [
            "elb-filter = elb_log_tools.filter:main",
            "elb-logs = elb_log_tools.logs:main",
            "elb-patterncounts = elb_log_tools.patterncounts:main",
        ]
    },
)
