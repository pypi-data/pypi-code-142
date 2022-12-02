# Copyright (c) 2019-2021 Thomas Kramer.
# SPDX-FileCopyrightText: 2022 Thomas Kramer
#
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(name='liberty-parser',
      version='0.0.15',
      description='Liberty format parser.',
      long_description=readme(),
      long_description_content_type="text/markdown",
      keywords='liberty parser',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
          'Programming Language :: Python :: 3'
      ],
      url='https://codeberg.org/tok/liberty-parser',
      author='T. Kramer',
      author_email='dont@spam.me',
      license='GPL-3.0-or-later',
      packages=find_packages(),
      install_requires=[
          'numpy==1.*',
          'sympy==1.6.*',
          'lark>=0.12.1'
      ],
      zip_safe=False)
