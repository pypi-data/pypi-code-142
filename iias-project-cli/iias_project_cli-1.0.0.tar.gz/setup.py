"""This is the installation toolset for this project."""
from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='iias_project_cli',
      version='1.0.0',
      author='Jules Debeaumont',
      description='A commandline interface for creating project structures',
      long_description=long_description,
      packages=find_packages(exclude=('tests',)),
      entry_points={
          'console_scripts': [
              'iias_project_cli = iias_project_cli.__main__:main'
          ]
      })
