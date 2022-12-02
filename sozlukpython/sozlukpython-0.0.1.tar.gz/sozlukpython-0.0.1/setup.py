from setuptools import setup, find_packages

setup(
    name="sozlukpython",
    version="0.0.1",
    description="A basic Turkish dictionary",
    long_description=open("README.md").read(),
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