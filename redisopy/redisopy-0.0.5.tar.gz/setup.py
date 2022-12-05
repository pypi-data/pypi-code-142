import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding='utf8') as fh:
    requires = fh.read().replace('==', '>=')

setuptools.setup(
    name="redisopy",
    version="0.0.5",
    author="Steven Wang",
    author_email="brightstar8284@icloud.com",
    description="python redis orm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StevenLianaL/redisopy",
    packages=setuptools.find_packages(exclude=["tests*"]),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
