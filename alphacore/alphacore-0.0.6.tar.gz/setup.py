#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="alphacore",
    version="0.0.6",
    description="Core statistical functions for alpha",
    author="Matthew Reid",
    author_email="alpha.reliability@gmail.com",
    license="LGPLv3",
    url="https://pypi.org/project/alphacore/",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
    install_requires=[
        "scipy>=1.7.0",
        "numpy>=1.19.2"
    ],
    python_requires=">=3.7",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*"]
    ),
)
