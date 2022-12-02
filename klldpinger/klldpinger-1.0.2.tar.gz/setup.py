from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='klldpinger',
    version='1.0.2',
    description='',
    author= '',
    url = 'https://klld.42web.io/',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['klld'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['klldPinger'],
    install_requires = [
          'aiohttp'
    ]
)
