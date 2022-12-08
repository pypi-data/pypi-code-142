from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='teste-de-funcionalidade-camera101',
    version=1.0,
    description='apenas para teste',
    long_description=Path('README.md').read_text(),
    author='GuilhermeCH',
    author_email='guilherme.santos.ch482@gmail.com',
    packages=find_packages()
)