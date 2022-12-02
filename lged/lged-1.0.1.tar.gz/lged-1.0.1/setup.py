from setuptools import setup, find_packages
from os import path

current_dir = path.abspath(path.dirname(__file__))

with open(path.join(current_dir, "requirements.txt")) as f:
    requirements = f.readlines()

with open(path.join(current_dir, "README.md"), "r", encoding="utf-8") as f:
    readme = f.read()
  
setup(
    name ='lged',
    version ='1.0.1',
    author ='Feilong Cui',
    author_email ='feilongcui@outlook.com',
    url ='https://github.com/bailang1208/lged',
    description ='Library Genesis EBook Downloader CLI Tool',
    long_description = readme,
    long_description_content_type ="text/markdown",
    license ='MIT',
    packages = find_packages(),
    entry_points ={'console_scripts': ['lged = lged.start:main']},
    classifiers =(
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords ='libgen python package lged',
    install_requires = requirements,
    zip_safe = False
)