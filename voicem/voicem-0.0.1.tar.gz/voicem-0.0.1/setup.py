import setuptools

from voicem.about import (
    __title__,
    __version__,
    __description__,
    __package_name__,
    __author__,
    __email__,
    __license__,
    __github__
)

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__github__,
    keywords="rssfeed, rssfeedcli, rssfeed-cli, discord-bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.1",
    # entry_points={
    #     "console_scripts": ["movens = movens.cli:main"],
    # },
)
