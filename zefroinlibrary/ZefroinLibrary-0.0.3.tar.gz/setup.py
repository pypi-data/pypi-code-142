from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Tools for Zefroin'
LONG_DESCRIPTION = 'Tools for Zefroin that are used throughout the project. CHANGELOG: Added new defs for ZefroinLib'

# Setting up
setup(
        name="ZefroinLibrary", 
        version=VERSION,
        author="AzureianGH",
        author_email="azureiangh@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'Zefroin', 'zss', 'zefroin', 'zf', 'zef', 'azureian'],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)