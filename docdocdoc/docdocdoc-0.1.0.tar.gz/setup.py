from setuptools import setup, find_packages

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="docdocdoc",
    version="0.1.0",
    description="A python library to template documentation from docstrings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/medialab/docdocdoc",
    license="MIT",
    author="Guillaume Plique, Laura Miguel",
    author_email="guillaume.plique@sciencespo.fr",
    keywords="documentation",
    python_requires=">=3.6",
    packages=find_packages(exclude=["test"]),
    package_data={"docs": ["README.md"]},
    install_requires=["docstring-parser==0.15"],
    zip_safe=True,
)
