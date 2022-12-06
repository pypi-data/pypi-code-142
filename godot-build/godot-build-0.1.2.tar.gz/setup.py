from os import path

from setuptools import find_packages, setup

with open(path.join(path.abspath(path.dirname(__file__)), "README.md"),
          "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="godot-build",
    version="0.1.2",
    description="Build tool for Godot projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://codeberg.org/Denotatum/gdbuild",
    author="snegg21",
    author_email="itsveter@gmail.com",
    license="GPL-3.0",
    license_files="LICENSE.md",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: Unix",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Utilities",
        "Topic :: Software Development",
    ],
    keywords="godot",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gdbuild=godot_build.gdbuild:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://codeberg.org/Denotatum/gdbuild/issues",
        "Source": "https://codeberg.org/Denotatum/gdbuild",
    },
)
