from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="rooster_client",
    version="0.0.1",
    description="Rooster Python client",
    scripts=["rooster"],
    url="https://github.com/productsupcom/rooster-python-sdk",
    author="Yorick Terweijden",
    author_email="yt@productsup.com",
    packages=["rooster_client"],
    install_requires=required,
    classifiers=[],
)
