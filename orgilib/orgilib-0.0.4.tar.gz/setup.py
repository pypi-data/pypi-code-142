import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="orgilib",
    version="0.0.4",
    author="Henry.Kim",
    author_email="hjkim@org-i.com",
    description="ORG-A py module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.org-i.com/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=['pandas>=1.4.4']
)