#!/usr/bin/env python3

from setuptools import setup
from pathlib import Path

setup(
    name='randstr-random',
    version='1.1.3',
    py_modules=['randstr'],
    license='MIT',
    description='Python package for generating strings with random characters.',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/CodeConfidant/randstr-random',
    author='Drew Hainer',
    author_email='codeconfidant@gmail.com',
    platforms=['Windows', 'Linux']
)

# - Update README.md
# - Update Version Number
# - Tar Wrap the Package: python setup.py sdist
# - Check Package: twine check dist/*
# - Upload to PYPI: twine upload dist/*
# - Commit Changes
# - Change Release Version in Github Repo