from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python Pygame Final Project'
LONG_DESCRIPTION = 'Final project for programming class. One level of Buper Bario Bro, which has no relation to Super Mario Bros. in any way shape or form'

# Setting up
setup(
        name="pyPlatFinal", 
        version=VERSION,
        author="Dylan Watson and Milo Moore",
        author_email="<jwatson8@g.emporia.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pygame'], # add any additional packages that 
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
