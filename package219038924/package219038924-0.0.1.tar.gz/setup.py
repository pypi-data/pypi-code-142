from os import path
from setuptools import setup

try:
    current_path = path.abspath(path.dirname(__file__))
except NameError:
    current_path = None

try:
    with open(path.join(current_path, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''


setup(
    name="package219038924",
    version="0.0.1",
    author="Averyanova_Margarita",
    author_email="margaritaaveryanova2004@gmail.com",
    description='binary search',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['package']
)
