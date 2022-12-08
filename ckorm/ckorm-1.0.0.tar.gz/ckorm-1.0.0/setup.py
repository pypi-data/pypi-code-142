from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = [
    "clickhouse-driver",
]

setup(
    name="ckorm",
    version="1.0.0",
    keywords=["Clickhouse", "ORM"],
    description="Clickhouse ORM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3 Licence",
    author="Lyle",
    author_email="lylemi@126.com",
    packages=find_packages(),
    install_requires=requires,
    platforms="any",
    scripts=[],
)
