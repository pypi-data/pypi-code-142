#!/Users/adilakhmetov/miniconda/bin/python3

import os
from setuptools import setup, find_packages

extras_require = {
    "develop": [
        "check-manifest",
        "pytest~=5.2",
        "pytest-cov~=2.8",
        "pytest-console-scripts~=0.2",
        "bumpversion~=0.5",
        "pyflakes",
        "pre-commit",
        "black",
        "twine",
    ],
}
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(
    extras_require=extras_require,
    entry_points={"console_scripts": ["qqr=qqr.commandline:qqr"]},
    install_requires=install_requires
)
