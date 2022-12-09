from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='safe_evaluation',  # package name
    version='0.1.10',  # version
    author="Lev Belous",
    author_email="leva22.08.01@inbox.ru",
    description='package solves expressions',  # short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lev4ek0/safe_eval',  # package URL
    install_requires=[
        'pandas',
        'numpy'
    ],  # list of packages this package depends
    # on.
    packages=find_packages(),  # List of module names that installing
    # this package will provide.
    python_requires='>=3.9',
)
