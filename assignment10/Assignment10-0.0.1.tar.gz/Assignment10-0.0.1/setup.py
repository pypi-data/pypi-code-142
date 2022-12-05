from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Assignment 10'
LONG_DESCRIPTION = 'This package can read a file and determine the value of the tweets'

# Setting up
setup(
        name="Assignment10", 
        version=VERSION,
        author="Milo Moore",
        author_email="<mmoore35@g.emporia.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'Assignment10'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)