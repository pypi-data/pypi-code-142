import os

from setuptools import setup, find_packages


version = os.getenv("PACKAGE_VERSION", "0.0.3a1")


setup(
    name='songpy',
    version=version,
    description='Package with objects representing objects of musical notation',
#    long_description=readme,
    author='Karol Ważny',
#    author_email='me@kennethreitz.com',
#    url='https://github.com/kennethreitz/samplemod',
#    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)