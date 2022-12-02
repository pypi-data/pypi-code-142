from setuptools import setup, find_packages

setup(
    name="sozlukpy",
    version="0.0.2",
    description="A basic Turkish dictionary",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    author="Meinos10",
    author_email="E.tmen2023@gmail.com",
    license="MIT",
    #classifiers = [
    #"Programming Language :: Python :: 3",
    #"License :: OSI Approved :: MIT License",
    #"Operating System :: OS Independent",
    #],
    keywords=["sozlukpy", "sozluk", "sozluk-python"],
    packages=find_packages(),
    requires=["requests"]
)