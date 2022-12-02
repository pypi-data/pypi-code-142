from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="birman",
    version="0.0.2",
    description="Multipart formdata decoder",
    packages=["birman"],
    py_modules=["birman"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/birman",
    author="Joe Gasewicz",
    author_email="joegasewicz@gmail.com",
)
