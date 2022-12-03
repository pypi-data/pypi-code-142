import setuptools
from setuptools import setup, find_packages
import os
# Set the proposed version number before committing
setup(name='rust-fastql',
    version=f'0.0.2',
    description='first',
    url='https://github.com/happy-machine/FastQL',
    author='happy-machine',
    author_email='freshbbk@me.com',
    license='MIT',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'rdflib',
        'pandas',
        'requests',
        'psycopg2-binary',
        'jinja2',
        'jprops'
    ],
    zip_safe=False)
      