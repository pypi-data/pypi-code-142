import os

from setuptools import setup, find_packages


version = os.getenv("PACKAGE_VERSION", "0.0.3a1")


license = open("LICENSE").read()


setup(
    name='songpy-latex-printer',
    version=version,
    description='Support package for package songpy, for printing formatted songbooks to intermediate latex files',
#    long_description=readme,
    author='Karol Ważny',
    python_requires='>=3.9',
#    author_email='me@kennethreitz.com',
#    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'latexprinter.resources': ["*"]},
    install_requires=['songpy']
)
