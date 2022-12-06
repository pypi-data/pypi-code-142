from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
    'viggocore>=1.0.0,<2.0.0',
    'flask-cors'
]

setup(
    name="viggolocal",
    version="1.1.2",
    summary='ViggoLocal Module Framework',
    description="ViggoLocal backend Flask REST service",
    packages=find_packages(exclude=["tests"]),
    install_requires=REQUIRED_PACKAGES
)
