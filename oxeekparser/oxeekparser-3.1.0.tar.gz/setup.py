import setuptools


with open('README.md', 'r') as file:
    long_description = file.read()

with open('requirements.txt', 'r') as file:
    requirements = file.read()

setuptools.setup(
    name="oxeekparser",
    version="3.1.0",
    author="oxeek",
    author_email="workkukin@gmail.com",
    description="Universal parser with using regex",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oxeekezy/universal-parser",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)


