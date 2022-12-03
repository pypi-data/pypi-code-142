from setuptools import find_packages, setup

from picsexl import __version__

with open("README.md", "r") as readme:
    long_description = readme.read()

with open("requirements.txt", "r") as requirements:
    install_requires = [line.rstrip() for line in requirements.readlines()]

setup(
    name="picsexl",
    version=".".join(str(v) for v in __version__),
    author="pog7x",
    author_email="poluningm@gmail.com",
    url="https://github.com/pog7x/picsexl",
    license="MIT",
    keywords="python calendar ics excel recurring",
    description="Converter from ics format to xls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["picsexl", "picsexl.*"]),
    python_requires=">=3.7",
    install_requires=install_requires,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
