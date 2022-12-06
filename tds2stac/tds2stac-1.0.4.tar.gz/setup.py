from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()



setup(
    name="tds2stac",
    version="1.0.4",
    description="TDS web services to STAC catalogs",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://codebase.helmholtz.cloud/cat4kit_dev/tds2stac",
    author="CAT4KIT Team",
    author_email="mostafa.hadizadeh@kit.edu",
    keywords="demo project",
    license="MIT",
    packages= find_packages(),
    install_requires=["pystac",
                        "lxml",
                        "Shapely",
                        "requests",
                        "pytz",
                        "python-dateutil",
                        "tqdm"],
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'tds2stac=tds2stac.cli:main'
        ]
    }    
)