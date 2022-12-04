from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='iFileIntersection',
    version='1.0.4',
    packages=['intersection'],
    include_package_data=True,
    description="Holds the utility finding common integers between two files",
    long_description="https://gitlab.com/nikhilkmdev/i-file-utils/-/blob/master/README.md",
    author='Nikhil K Madhusudhan (nikhilkmdev)',
    author_email='nikhilkmdev@gmail.com',
    maintainer='Nikhil K Madhusudhan (nikhilkmdev)',
    maintainer_email='nikhilkmdev@gmail.com',
    keywords=['intersection', 'huge', 'files', 'python3'],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    requires=[],
)
