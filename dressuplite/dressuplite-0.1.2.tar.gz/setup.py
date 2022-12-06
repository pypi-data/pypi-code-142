"""Package installation setup."""
import os
import re
from pathlib import Path
from typing import Match, cast

from setuptools import setup

_DIR = Path(__file__).parent
_PACKAGE_NAME = "dressuplite"

setup(
    name=_PACKAGE_NAME,
    author="Ouroboros Chrysopoeia",
    author_email="impredicative@users.nomail.github.com",
    version=cast(Match, re.fullmatch(r"refs/tags/v?(?P<ver>\S+)", os.environ["GITHUB_REF"]))["ver"],  # Ex: GITHUB_REF="refs/tags/1.2.3"; version="1.2.3"
    description='Dependency-free lightweight fork of the package "dressup" to convert strings to use Unicode formatting',
    keywords="unicode text",
    long_description=(_DIR / "README.md").read_text().strip(),
    long_description_content_type="text/markdown",
    url="https://github.com/impredicative/dressuplite/",
    packages=[_PACKAGE_NAME],
    package_data={_PACKAGE_NAME: ["translator.toml"]},
    python_requires=">=3.11",
    classifiers=[  # https://pypi.org/classifiers/
        # For feature compatibility, see https://nedbatchelder.com/text/which-py.html
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing :: General",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
