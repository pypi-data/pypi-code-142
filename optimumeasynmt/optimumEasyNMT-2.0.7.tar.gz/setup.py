import platform
import sys
from os import path

import pkg_resources
from setuptools import find_packages
from setuptools import setup

def get_requirements_list(f):
    with open(f) as requirements_txt:
        requirements_list = [
            str(requirement)
            for requirement in pkg_resources.parse_requirements(requirements_txt)
        ]
        return requirements_list


with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

install_requires = get_requirements_list('requirements.txt')

setup(
    name="optimumEasyNMT",
    version="2.0.7",
    author="Nils Reimers",
    author_email="info@nils-reimers.de",
    description="Easy to use state-of-the-art Neural Machine Translation",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/UKPLab/EasyNMT",
    download_url="https://github.com/UKPLab/EasyNMT/archive/v2.0.2.zip",
    # packages=[
    #     "easynmt"
    # ],
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    keywords="Neural Machine Translation"
)
