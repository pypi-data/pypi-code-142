import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kadena_sdk",
    version="1.0.0",
    author="Luzzotica",
    author_email="sterlinglong0@gmail.com",
    description="A simple SDK for interacting with the Kadena Blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Luzzotica/KadenaPythonSdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)