import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="TinyDataAnalyticsTool",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    # Full name of the author
    author="Efstratios Pahis",
    description="Disclaimer: This is an old Project from when I started learning Python from 2019 (not the best written code). A GUI for flexibly organizing Data Analytics related tasks/functions and adding custom User Input Fields if needed.",
    # Long description read from the the readme file
    long_description=long_description,
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    license='MIT',
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["tinydataanalyticstool"],             # Name of the python package
    # Directory of the source code of the package
    url="https://github.com/efstratios97/Tiny-Data-Analytics-Tool",
    install_requires=["pandas",
                      "matplotlib"]                     # Install other dependencies if any
)
