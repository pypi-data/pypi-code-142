import setuptools
# The directory containing this file
import pathlib
HERE = pathlib.Path(__file__).parent
from setuptools import find_packages, setup

# The text of the README file
README = (HERE / "README.md").read_text()
setup(
    name="pbl6packageg2",
    version="0.0.1",
    author="Group2",
    description="PBL6",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=[
        'pbl6packageg2.config',
        'pbl6packageg2.emailhelper',
    ],
    license='MIT',
    url="https://github.com/banhmysuawx/PBL6-BE",
    keywords=["django", "djangorestframework", "drf", "rest-client",],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)