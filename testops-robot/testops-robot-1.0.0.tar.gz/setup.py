import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRES=[
    "testops-commons>=1.0.6"
]

setuptools.setup(
    name="testops-robot",
    version="1.0.0",
    author="Katalon, LLC. (https://www.katalon.io)",
    author_email="info@katalon.io",
    description="Katalon TestOps Robot Plugin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/katalon-studio/testops-robot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords=["Katalon", "TestOps"],
    python_requires='>=3.6',
    install_requires=REQUIRES
)
