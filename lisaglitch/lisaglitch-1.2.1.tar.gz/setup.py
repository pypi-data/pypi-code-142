#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-module-docstring,exec-used

import setuptools


with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='lisaglitch',
    use_scm_version=True,
    author='Jean-Baptiste Bayle',
    author_email='j2b.bayle@gmail.com',
    description="LISA Glitch generates glitch files to be injected in the instrument simulation with LISANode.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.in2p3.fr/lisa-simulation/glitch",
    license='BSD-3-Clause',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'h5py',
        'numpy',
        'scipy',
        'matplotlib',
        'torch',
        'importlib_resources',
        'importlib_metadata',
    ],
    setup_requires=['setuptools_scm'],
    tests_require=['pytest'],
    python_requires='>=3.7',
)
