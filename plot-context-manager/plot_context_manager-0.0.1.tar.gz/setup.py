import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["matplotlib>3,<4"]

setuptools.setup(
    name="plot_context_manager",
    version="0.0.1",
    author="Albert Farkhutdinov",
    author_email="albertfarhutdinov@gmail.com",
    description=(
        "The package to work with plots as with context managers."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlbertFarkhutdinov/plot_context_manager",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
