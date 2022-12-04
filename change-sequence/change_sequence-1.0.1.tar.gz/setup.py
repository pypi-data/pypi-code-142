"""setup.py"""
from os import path
from setuptools import setup

try:
    current_path = path.abspath(path.dirname(__file__))
except NameError:
    current_path = None
try:
    with open(path.join(current_path, 'README.md'),
              encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = '''This is a simple package for converting strings
                        big in little and vice versa'''
setup(
    name='change_sequence',
    version='1.0.1',
    # list folders, not files
    packages=['change_sequence'],
    scripts=['change_sequence/test_convs.py'],
    license='MIT License',
    description='Converting strings project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    requires=['pytest'],
)
