"""Setup config."""

# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import versioneer


requires = []

if __name__ == "__main__":
    setup(
        name="magicbag",
        url="https://github.com/lipicoder/magicbag",
        author="lipi",
        author_email="lipicoder@qq.com",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        packages=find_packages(),
        include_package_data=True,
        install_requires=requires,
    )
