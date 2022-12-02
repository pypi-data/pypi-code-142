import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydstir",
    version="1.2.3",
    author="Bernard Namou",
    author_email="zalkoweb@anarchydev.com",
    description="a module for pydstir tool from discord",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://anarchydev.com",
    packages=['pydstir'],
    install_requires=['setuptools', 'columnar>=1.3.1', 'colorama'],
    package_data={'pydstir': ['*.json']},
    entry_points={
        'console_scripts': ['pydstir-color=pydstir.main:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
