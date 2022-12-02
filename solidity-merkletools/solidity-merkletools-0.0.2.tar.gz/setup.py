import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="solidity-merkletools",
    version="0.0.2",
    description="Merkle Tools",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url="https://github.com/f8n/solidity-pymerkletools",
    author="Hsu Han Ooi",
    keywords="merkle tree, blockchain",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    include_package_data=False,
    zip_safe=False,
)
