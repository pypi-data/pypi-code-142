import setuptools
setuptools.setup(
    name="tb_bot",                     # This is the name of the package
    version="0.0.5",                        # The initial release version
    author="Freak",                     # Full name of the author
    description="get tor file",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
)