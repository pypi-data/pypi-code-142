import os

from setuptools import find_packages, setup


HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(HERE, "api/README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Get the requirements
with open("api/requirements.txt", "r", encoding="utf-8") as requirement_file:
    requirements = requirement_file.readlines()

setup(
    name='nlp_ood',
    version='0.1.1',
    description='domain classification',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Developer',
    license='MIT',
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.7",
    packages=['api'],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

