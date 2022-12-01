import setuptools

with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRES=[
]

setuptools.setup(
    name="pypi-robot-visible",
    version="1.0.0",
    author="Tuan, LLC",
    author_email="anhtuantatt@gmail.com",
    description="Pypi Visible",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuananht/pypi-robot-visible",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords=["Tuan", "Visible"],
    python_requires='>=3.6',
    install_requires=REQUIRES
)