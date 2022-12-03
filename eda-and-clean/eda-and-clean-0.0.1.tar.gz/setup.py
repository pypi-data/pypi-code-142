import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eda-and-clean",
    version="0.0.1",
    author="Aravind Ganesan",
    author_email="1988.aravind@gmail.com",
    description="A package of automation tools for EDA and cleaning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aravindganesan88/eda_and_clean",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[""],
    python_requires=">=3.7",
)
