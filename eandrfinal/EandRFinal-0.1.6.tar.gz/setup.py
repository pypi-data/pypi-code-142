from setuptools import setup, find_packages

VERSION = '0.1.6' 
DESCRIPTION = 'A game to tease your brain.'
LONG_DESCRIPTION = 'This game resembles the Impossible Quiz. We added our own spin on it using the PyGame library.'

# Setting up
setup(
        name="EandRFinal", 
        version=VERSION,
        author="Emma Hall",
        author_email="<elohall01@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
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