from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='klldpinger',
    version='1.0.3',
    description='',
    author= 'klld',
    url = 'https://pinger.klld.tk/',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['klld'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['klldpinger'],
    install_requires = [
          'aiohttp'
    ]
)
