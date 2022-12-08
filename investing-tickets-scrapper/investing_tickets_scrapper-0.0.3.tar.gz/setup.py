from setuptools import setup, find_packages

DESCRIPTION = 'Scraps stock tickets from "Investing.com" using Selenium and parse using BeautifulSoup'
with open("README.md", "r") as rdm:
    LONG_DESCRIPTION = rdm.read()

# Setting up
setup(
    name="investing_tickets_scrapper",
    version='0.0.3',
    author="Lucas Rocha",
    author_email="lucasrocha.png@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["investing_tickets_scrapper"],
    install_requires=['pandas>=1.3.3', 'selenium>=4.1.3', 'beautifulsoup4>=4.4.1'],
    keywords=['python', 'tickers', 'index', 'stocks', 'exchange', 'investing'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)