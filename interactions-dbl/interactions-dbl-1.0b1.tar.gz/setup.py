import re

from setuptools import setup

with open("interactions/ext/dbl/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

requirements = [
	"aiohttp~=3.8.0",
	"discord-py-interactions~=4.3.0"
]

setup(
    name="interactions-dbl",
    version=version,
    description="DBL (Discord Bot Lists) extension library for discord-py-interactions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahul-nanwani/interactions-dbl",
    project_urls={
        "Bug Tracker": "https://github.com/rahul-nanwani/interactions-dbl.git"
    },
    author="Rahul Nanwani",
    author_email="rahulnanwani@icloud.com",
    license="MIT",
    packages=["interactions.ext.dbl"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    install_requires=requirements,
)
