from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="taxOrder",
    version="0.1",
    #python_requires='>=3.7.0',
    description="Returns list of species in a phylogenetic tree ordered by increasing taxonomic distance to a reference species",
    author="Felix Langschied",
    author_email="langschied@bio.uni-frankfurt.de",
    packages=find_packages(),
    package_data={'': ['*']},
    install_requires=[
        'ete3',
        'six',
        'numpy'
    ],
    license="GPL-3.0",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
    ],
)
