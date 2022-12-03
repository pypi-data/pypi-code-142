from setuptools import setup, find_packages
from pathlib import Path


setup(
    name='KingDataGenerator',
    version=1.3,
    description="This packet generates fictitious human data, uniquely (names,emails,password,personal-documents), for the use of the develpoer",
    long_description=Path('README.md').read_text(),
    author='Black King',
    keywords={'data human', 'generator', 'gerador', 'dados pessoais', 'fordev', '4dev'},
    packages=find_packages()
)