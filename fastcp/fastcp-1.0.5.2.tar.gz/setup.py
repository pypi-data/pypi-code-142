import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "fastcp",
    version = "1.0.5.2",
    author = "Avinash Doddi",
    author_email = "avinashdoddi2001@gmail.com",
    description = "A Python Package for Competitive Programming",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/avinash-doddi/fastcp.git",
    project_urls = {
        "Bug Tracker": "https://github.com/avinash-doddi/fastcp.git",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "fastcp"},
    packages = setuptools.find_packages(where="fastcp"),
    python_requires = ">=3.6"
)