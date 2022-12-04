import setuptools

setuptools.setup(
    name="googlesearch.py",
    version="1.5",
    description="The search API for Google.",
    long_description=str(open("README.md", "r", encoding="utf-8").read()),
    long_description_content_type="text/markdown",
    keywords = "googlesearch.py, python google search, google search pypi, google api",
    package=setuptools.find_packages(where="src"),
    install_requires = ["bs4"],
    python_requires=">=3.6"
)