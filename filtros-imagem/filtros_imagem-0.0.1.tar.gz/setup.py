from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="filtros_imagem",
    version="0.0.1",
    author="m. caponera",
    author_email="m.caponera@gmail.com",
    description="Pequeno pacote com filtros simples.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcaponera/filtros-imagem",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)