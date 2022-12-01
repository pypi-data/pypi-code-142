from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='lognwrite',
    version='0.1.3',
    license='MIT',
    author="Muhammad Alif Putra Yasa",
    author_email='malifputrayasa@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/malifpy/log-n-write',
    keywords='log',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'typing_extensions',
    ],
)
