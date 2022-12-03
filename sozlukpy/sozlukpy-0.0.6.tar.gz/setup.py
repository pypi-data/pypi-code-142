from setuptools import setup, find_packages

setup(
    name="sozlukpy",
    version="0.0.6",
    description="A basic Turkish dictionary",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    author="Emre",
    author_email="E.tmen2023@gmail.com",
    license="MIT",
    #classifiers = [
    #"Programming Language :: Python :: 3",
    #"License :: OSI Approved :: MIT License",
    #"Operating System :: OS Independent",
    #],
    keywords=["sozlukpy","sozlukpython", "sozluk", "sozluk-python", "sozluk-py"],
    packages=find_packages(),
    requires=["requests"]
)