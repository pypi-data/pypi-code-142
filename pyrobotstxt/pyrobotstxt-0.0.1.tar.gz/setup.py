from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = "0.0.1"

setup(
    name="pyrobotstxt",
    version=version,
    author="Faisal Shahzad",
    author_email="seowingsorg@gmail.com",
    description="Python Package to Generate and Analyse Robots.txt files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.seowings.org/",
    project_urls={
        "Bug Tracker": "https://github.com/seowings/pyrobotstxt/issues",
        "Documentation": "https://pyrobotstxt.seowings.org/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["pyrobotstxt"],
    python_requires=">=3.9",
    install_requires=["pillow==9.3.0"]
)