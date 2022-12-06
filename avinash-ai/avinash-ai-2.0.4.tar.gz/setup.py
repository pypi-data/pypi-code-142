from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="avinash-ai",
    version="2.0.4",
    description="Build your own ML",
    packages=["avinash_ai"],
    install_requires=["openai"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)

