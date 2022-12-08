from setuptools import setup

setup(
    name="tileputty",
    version="0.2.10",
    description="Tool to upload a tile cache to AWS S3",
    url="https://github.com/wri/tileputty",
    packages=["tileputty"],
    author="Thomas Maschler",
    author_email="thomas.maschler@wri.org",
    license="MIT",
    install_requires=["boto3>=1.16.55", "typer>=0.4.0", "parallelpipe>=0.3.0"],
    entry_points={"console_scripts": ["tileputty=tileputty.upload_tiles:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
