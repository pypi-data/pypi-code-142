from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Tweet Sentiment Assignment 10'
LONG_DESCRIPTION = 'Tweet sentiment analysis package for Python programming assignment for my class'

# Setting up
setup(
        name="TweetSentim", 
        version=VERSION,
        author="Dylan Watson",
        author_email="<jwatson8@g.emporia.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires = [], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'simpleCalpackage'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
