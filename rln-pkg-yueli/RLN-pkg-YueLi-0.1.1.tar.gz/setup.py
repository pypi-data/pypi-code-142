import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RLN-pkg-YueLi", # Replace with your own username
    version="0.1.1",
    author="Yue Li",
    description="RLN package in Incorporating the image formation process into deep learning improves network performance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MeatyPlus/RLN-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)