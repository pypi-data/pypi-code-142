import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bind-sdk",
    version="1.0.0",
    author="Gustavo Ghioldi",
    author_email="gustavoghioldi@gmail.com",
    description="Easy integration with BIND Argentina",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gustavoghioldi/bind-sdk-python",
    packages=setuptools.find_packages(),
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
