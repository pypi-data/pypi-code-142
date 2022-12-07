import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "audacianumberrecognition",
    version = "0.0.3",
    author = "Audacia",
    author_email = "audacia@unisimonbolivar.edu.co",
    description = "Audacia Recognition Number",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = [
        "paddleocr",
        "paddlepaddle",
    ],
    url = "https://gitlab.com/audaciastudio/audacianumberrecognition",
    project_urls = {
        "Bug Tracker": "https://gitlab.com/audaciastudio/audacianumberrecognition",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    package_data={"audacianumberrecognition": ['fonts/*']},
    python_requires = ">=3.9"
)