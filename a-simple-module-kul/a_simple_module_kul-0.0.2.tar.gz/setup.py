from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'my first python package'
LONG_DESCRIPTION = 'The first python package I ever created, it has functionality to do basic math operations.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="a_simple_module_kul", 
        version=VERSION,
        author="Stijn Dom",
        author_email="stijn.dom@hotmail.be",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'numpy'
        
        keywords=['python', 'first package', 'math', 'university'],
        classifiers= [
            "Development Status :: 1 - Planning",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)