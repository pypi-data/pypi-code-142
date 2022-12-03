from setuptools import setup, find_packages
from pathlib import Path


setup(
    name='KingDataGenerators',
    version=1.2,
    description="This packet generates fictitious human data, uniquely (names,emails,password,personal-documents), for the use of the develpoer",
    long_description=Path('README.md').read_text(),
    author='Black King',
    author_email='docomeco2k20@gmail.com',
    keywords={'data human', 'generator', 'gerador', 'dados pessoais', 'fordev', '4dev'},
    packages=find_packages()
)