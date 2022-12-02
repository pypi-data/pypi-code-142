'''
commands 
python setup.py sdist bdist_wheel
python -m twine upload --repository pypi dist/*
'''

import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="bbcinds",                     # This is the name of the package
    version="0.0.6",                        # The initial release version
    author="Balaji Betadur",                     # Full name of the author
    description="BBC indicator and custom functions",
    long_description="BBC indicator and custom functions",      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["bbcinds"],             # Name of the python package
    package_dir={'':'bbcinds/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)