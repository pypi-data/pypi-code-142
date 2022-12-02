from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='pysmells',
    version='0.0.1',
    url='https://github.com/marcos-de-sousa/pysmells',
    license='MIT License',
    author='Marcos Paulo Alves de Sousa, Marco Aurélio Proença Neto',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='desousa.mpa@gmail.com, marconeto3000@gmail.com',
    keywords='Pacote',
    description='Um pacote em python para analisa vunerabilidades de programas em python',
    packages=['pysmells'],
    install_requires=['numpy','pandas',],)