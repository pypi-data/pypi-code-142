from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="factorial_fab",
    version="0.0.1",
    author="Fabricio",
    author_email="fabricioeirim@gmail.com",
    description="Calculo fatorial utilizando o modulo fatorial da lib math",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fabricioeirim/package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)