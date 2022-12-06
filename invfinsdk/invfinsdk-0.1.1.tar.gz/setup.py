#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("invfinsdk/__version__.py") as version_file:
    version = version_file.read()
    version = version[-7:-2]

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = [
    "requests",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Lucas Montes",
    author_email="lluc23@hotmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="An SDK to interact with InvFin endpoints",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="invfinsdk",
    name="invfinsdk",
    packages=find_packages(include=["invfinsdk", "invfinsdk.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/InvFin/Python-sdk",
    version=version,
    zip_safe=False,
)
