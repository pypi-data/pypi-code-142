import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyconl",
    version="0.4.3",
    author="Jara van Veldhoven",
    author_email="jarav@nveldhoven.nl",
    description="Civiel Technisch ontwerpen in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ornor/pyco",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: Dutch",
    ],
)
