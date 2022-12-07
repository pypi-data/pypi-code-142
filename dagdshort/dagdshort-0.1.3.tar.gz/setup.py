"""Package installation setup."""
import os
import re
from pathlib import Path
from typing import Match, cast

from setuptools import find_packages, setup

_DIR = Path(__file__).parent


def parse_requirements(file_path: Path) -> list[str]:
    """Return requirements from requirements file."""
    # Ref: https://stackoverflow.com/a/50368460/
    with open(file_path) as file:
        return [r for r in [line.split("#", 1)[0].strip() for line in file] if r]


setup(
    name="dagdshort",
    author="Ouroboros Chrysopoeia",
    author_email="impredicative@users.nomail.github.com",
    version=cast(Match, re.fullmatch(r"refs/tags/v?(?P<ver>\S+)", os.environ["GITHUB_REF"]))["ver"],  # Ex: GITHUB_REF="refs/tags/1.2.3"; version="1.2.3"
    description="Multithreaded concurrent da.gd URL shortener with in-memory cache",
    keywords="da.gd url shortener",
    long_description=(_DIR / "README.md").read_text().strip(),
    long_description_content_type="text/markdown",
    url="https://github.com/impredicative/dagdshort/",
    packages=find_packages(exclude=["scripts"]),
    install_requires=parse_requirements(_DIR / "requirements/install.in"),
    python_requires=">=3.9",
    classifiers=[  # https://pypi.org/classifiers/
        # For feature compatibility, see https://nedbatchelder.com/text/which-py.html
        # "Programming Language :: Python :: 3.8",  # Has numerous pytest errors.
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
