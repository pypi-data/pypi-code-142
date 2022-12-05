from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Assignment 10'
LONG_DESCRIPTION = 'My submission for CS501 assignment 10'

# Setting up
setup(
        name="mregancs501a10py", 
        version='0.0.1',
        author="Mitch Regan",
        author_email="<mregan1@g.emporia.com>",
        description="Assignment 10",
        long_description="My submission for CS501 assignment 10",
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)