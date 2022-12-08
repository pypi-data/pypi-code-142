from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="fun2py",
    version="0.0.2",
    author="Tao Xiang",
    author_email="tao.xiang@tum.de",
    description="A package for functional programming in python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/leoxiang66/functional-programming/tree/pyfp",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
  "Programming Language :: Python :: 3.8",
  "License :: OSI Approved :: MIT License",
    ],
)