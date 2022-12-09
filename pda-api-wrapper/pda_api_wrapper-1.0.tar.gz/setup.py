from setuptools import setup

setup(
    name='pda_api_wrapper',
    version='1.0',
    description='Python wrapper for the PowerDNS Administrator (PDA) API',
    author='Bernward Sanchez',
    author_email='contact@bern.codes',
    packages=['pda_api_wrapper'],
    install_requires=['requests'],
)
