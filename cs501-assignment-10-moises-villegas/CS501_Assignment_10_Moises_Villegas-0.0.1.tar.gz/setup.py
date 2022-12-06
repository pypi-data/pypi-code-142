from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Assignment 10'
LONG_DESCRIPTION = 'CS 501 Assignment 10 Submission - Moises Villegas'

# Setting up
setup(
        name="CS501_Assignment_10_Moises_Villegas", 
        version=VERSION,
        author="Moises Villegas",
        author_email="<mvilleg1@g.emporia.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'Assignment 10'],
        classifiers= [
            "Programming Language :: Python :: 3"
        ]
)