from setuptools import setup

setup(
    name="pypi-project-no-meta",
    version="0.1.0",
    author="pilosus",
    packages=["pypi_project_no_meta"],
    package_dir={"pypi_project_no_meta": "./src/pypi_project_no_meta"},
    description="PyPI minimal project with no meta",
)
