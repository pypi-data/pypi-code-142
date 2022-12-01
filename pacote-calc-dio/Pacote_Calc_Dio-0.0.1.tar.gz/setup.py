from setuptools import setup

from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='Pacote_Calc_Dio',
    version='0.0.1',
    license='MIT License',
    author='Gilmar_Alexandre',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='gilmar.alexandre.sc@outlook.com',
    keywords='Calculadora_gilmar',
    description=u'Calculadora',
    packages=['Calculadora_gilmar'],)