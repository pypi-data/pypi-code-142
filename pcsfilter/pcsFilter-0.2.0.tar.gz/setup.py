from setuptools import find_packages, setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="pcsFilter",
    version="0.2.0",
    python_requires=">=3.7",
    author="Sasha Bondarev (Oleksandr)",
    author_email="alex.d.bondarev@gmail.com",
    license="MIT",
    description="Tool for filtering out stinky/smelling code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alex-d-bondarev/pcsFilter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "blue~=0.9.0",
        "click~=8.0.0",
        "ConfigUpdater~=3.0.0",
        "flake8>=3.8,<5.0.0",
        "isort~=5.10.0",
        "radon~=5.1.0",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={
        "console_scripts": [
            "pcsFilter=src.pcsFilter.cli:main",
        ]
    },
)
