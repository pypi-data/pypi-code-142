import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indonesianearthquake",
    version="0.1",
    author="Octavio",
    author_email="prayudhaocto@gmail.com",
    descriptions="This package use BeautifulSoup4 and Requests, "
                 "it can produce output in JSON that is ready to be used in web or mobile applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/remotebandungid/BMKG_REPORT_EARTHQUAKE",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
