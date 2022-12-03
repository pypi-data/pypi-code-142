from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'a basic good looking coinmarketcap scraper by HP Team'
LONG_DESCRIPTION = 'this package allows you to scrape coinmarketcap.com for name symbol price and logo if wanted'

# Setting up
setup(
    name="coinmarketcap_scraper_hp",
    version=VERSION,
    author="hirbod (hirbodprime)",
    author_email="hirbodprime@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4', 'colorama'],
    keywords=['python', 'scraper', 'coinmarketcap', 'coinmarketcap scraper', 'beautifulsoup'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)