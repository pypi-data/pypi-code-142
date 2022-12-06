from setuptools import setup, find_packages

from codecs import open
from os import path 

HERE=path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Juan_Cuadrado_Test_B',
    packages=find_packages(include=['Task_B_library']),
    version='0.1.0',
    long_description="Check if a library version is equal, greater or less than other", 
    description='Check Version Library Comparison Library',
    author='Juan Pablo Cuadrado',
    license='MIT',
    include_package_data=True,
    install_requires=["numpy"],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest==4.4.1'],
    test_suite='tests'
)    
