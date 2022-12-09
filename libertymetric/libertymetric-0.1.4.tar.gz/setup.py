import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = 'libertymetric',
    version = '0.1.4',
    author = 'hockchen',
    author_email = 'hock.chen@dipsci.com',
    description = 'Liberty Metric Utility',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/dipsci/liberty',
    packages=setuptools.find_packages(),
    keywords = ['liberty','metric','timing','EDA','physical design'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)