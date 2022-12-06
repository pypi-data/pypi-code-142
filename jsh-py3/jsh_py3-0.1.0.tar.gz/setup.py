import os
from setuptools import setup

with open("README.rst") as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="jsh_py3",
    packages=["jsh_py3"],
    version="0.1.0",
    description="Junos-like shell library for Python 3",
    author="A-c0rN",
    author_email="acrn@gwes-eas.network",
    license="ODbL-1.0",
    install_requires=["six", "readline"],
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/A-c0rN/jsh_py3",
    keywords="audio sound eas alerting emergency-alert-system",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
