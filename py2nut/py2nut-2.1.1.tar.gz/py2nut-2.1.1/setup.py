import pathlib
from setuptools import setup, find_packages
import py2Nut

# The text of the README file
ME_PATH = pathlib.Path(__file__).parent
README = (ME_PATH / "README.md").read_text()
NAME = "py2nut"
VERSION = py2Nut.__version__


# This call to setup() does all the work
setup(
    name = NAME,
    version = VERSION,
    description = "This Library allows you to make Misc operations in various domain",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Laurent-Tupin/py2nut",
    author = "Laurent Tupin",
    author_email = "laurent.tupinn@gmail.com",
    license = "Copyright 2022-2035",
    classifiers=[
        "License :: Free For Home Use",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages = find_packages(include=("pynut_1tools",), exclude = ("test",)),
    include_package_data = True,
    install_requires = ["pandas==1.1.3"]
    # ,entry_points={"console_scripts": ["EXEnameFile=FolderName.__main__:main"]}
)
