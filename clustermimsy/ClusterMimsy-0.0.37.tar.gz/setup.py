from setuptools import setup, find_packages

VERSION = '0.0.37' 
DESCRIPTION = 'A package for the ClusterMI algorithm'
LONG_DESCRIPTION = 'A package for the ClusterMI algorithm'

# Setting up
setup(
        name="ClusterMimsy", 
        version=VERSION,
        author="ClusterMimsyDev",
        author_email="<ClusterMimsyDev@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=['ClusterMimsy', 'ClusterMimsy.nest'],
        install_requires=[
            'numpy','pandas', 'scipy', 'scikit-learn'
        ], # add any additional packages that 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)