from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Sentiment Finder for tweets'
LONG_DESCRIPTION = 'Finds whether tweets are positive, negative, or neutral and outputs a ratio'

# Setting up
setup(
        name="Assign10tnguyen4", 
        version=VERSION,
        author="Tommy Nguyen",
        author_email="<tnguyen4@g.emporia.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'sentimentFinder'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)