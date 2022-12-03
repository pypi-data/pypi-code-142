#!/usr/bin/env python
import os
from setuptools import setup, find_packages



install_requires = [
    "argparse",
    "numpy>=1.18.4",
    "scikit-learn>=0.23.1",
    "scipy>=1.4.1",
    "torch>=1.5.0",
    "pytorch-lightning>=1.0.3",
]

readme = open("README.md").read()



setup(name='GSAE',
      version='0.2',
      description='Graph Scattering Autoencoder',
      author='Egbert Castro',
      author_email='egbert.castro@yale.edu',
      url='https://github.com/KrishnaswamyLab/GSAE',
      install_requires=install_requires,
      long_description=readme,
      packages=find_packages()
      )


