import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

REQUIRES_PYTHON = '>=3.6.0'


# This call to setup() does all the work
setup(
    name="probNORM",
    version="1.0.3",
    description="Method for structural probing signal calculation that eliminates read distribution bias and prevents reactivity underestimation.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zywicki-lab/probNORM",
    author="Agnieszka Chełkowska-Pauszek",
    python_requires=REQUIRES_PYTHON,
    author_email="agnieszka.chelkowska@amu.edu.pl",
    license="GNU General Public License v3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    dependencies = [
    "pysam",
    "numpy",
    'scipy',
    ],
    install_requires = [
        "pysam",
    "numpy",
    'scipy',
    ],
    packages=find_packages(),
    include_package_data=True,
    scripts=['probNORM-pkg/input_probnorm', 'probNORM-pkg/probnorm'],

)
