import setuptools

setuptools.setup(
    name="easydb-json",
    version="1.0.0",
    author="Lactua",
    author_email="lactua@lactua.com",
    description="A simple way to handle database in json.",
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lactua/easydb-json",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)