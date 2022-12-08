import os
import setuptools


def get_version() -> str:
    """returns current version of the project

    :return: Current version of the project
    :rtype: str
    """
    init_filename = os.path.join(
        os.path.dirname(__file__), "metaibricks", "__init__.py"
    )
    with open(init_filename, "r") as fp:
        version_line = next(
            line for line in fp.readlines() if line.startswith("__version__ =")
        )
    return version_line.split()[-1].strip('"')


with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="metaibricks",
    version=get_version(),
    author="LabIA-MF",
    author_email="lab_ia@meteo.fr",
    description="Met-AI-Bricks : Meteorological AI Bricks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab.meteo.fr/deep_learning/ai-lab-tools/met-ai-bricks",
    packages=setuptools.find_packages(),
    install_requires=[
        "pydantic",
        "requests",
        "beautifulsoup4",
        "mflog",
    ],
)
