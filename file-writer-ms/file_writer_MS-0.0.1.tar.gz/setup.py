from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'File Writer package'
LONG_DESCRIPTION = 'File writer package written by Mohsen Sadi'

# Setting up
setup(
       
        name="file_writer_MS", 
        version=VERSION,
        author="Mohsen Sadi",
        author_email="<mohsen.sadi@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        keywords=['python',],
        classifiers= [
            "Development Status :: 3 - Alpha",
            
        ]
)