import setuptools
from os.path import join, dirname

setuptools.setup(
    name='insrt',
    version='1.0',
    packages=setuptools.find_packages(),
    author='Danila Kashtanov',
    long_description=open(join(dirname(__file__), 'readme.md')).read(),
)
