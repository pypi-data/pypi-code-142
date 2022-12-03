import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

# use https://dillinger.io/ para ver como vai ficar sua documentação (README.md) em
# markdown.

setuptools.setup(
    name="modularizador",
    version="1.0.7",
    author="Heitor Leal Farnese",
    author_email="heitor.leal.farnese@gmail.com",
    description="Importe arquivos .ipynb como se fossem arquivos .py no Jupyter Notebook | Import .ipynb files as if they were .py files on Jupyter Notebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    keywords='módulos ipynb jupyter notebook py importar importação import importation importing modules ipython',
#     packages=setuptools.find_packages(), # Aqui entra uma lista de nomes de subpastas que por ventura fossem módulos
    packages=['modularizador'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    )

# Acesse https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/ para saber mais sobre a função setup e seus argumentos


# A instalação ocorre com o comando
# python setup.py install
# utilizado a partir do diretório onde se encontra setup.py

# Para instalar no Jupyter Notebook, vá lá e digite
# !python setup.py install

# Porém, esta forma está deprecada. A forma correta moderna é criar uma versão
# comprimida do seu pacote: um wheel. Primeiro, atualize o setuptool wheel via
# !python -m pip install --user --upgrade setuptools wheel
# Ou, no jupyter notebook:
# !pip install --user --upgrade setuptools wheel
# Depois execute o comando
# !python setup.py sdist bdist_wheel
