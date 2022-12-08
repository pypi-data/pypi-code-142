from setuptools import find_packages, setup

setup(
   name='mop_utils',
   version='1.1',
   description='Utilities for MOP',
   packages=['mop_utils'],
   package_dir={'mop_utils': './src/mop-utils'},
   python_requires='>=3.8.0'
)