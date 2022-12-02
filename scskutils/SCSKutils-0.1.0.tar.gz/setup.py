from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'SCSK DX data team utils package.'
LONG_DESCRIPTION = 'SCSK DX data team utils package.'

# Setting up
setup(
    name="SCSKutils",
    version=VERSION,
    author="emelas (Elias Melas)",
    author_email="<elias.melas@scskeu.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['sqlalchemy','pyodbc','deep_translator'],
)