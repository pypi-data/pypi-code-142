from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description  =  fh.read()

setup(
    name = 'phyengine',
    version = '1.2.5',
    description  =  'Pyhton library for simple physics modelation',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/tacterex/PhyEngine',
    author = 'tacterex',
    license = 'MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
    ]
)