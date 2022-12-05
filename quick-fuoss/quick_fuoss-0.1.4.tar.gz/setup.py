import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quick_fuoss",
    packages=["quick_fuoss"],
    version="0.1.4",
    author="Corin Wagen",
    author_email="corin.wagen@gmail.com",
    license="Apache 2.0",
    description="rapid estimation of ion-pair dissociation constants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/corinwagen/quick-fuoss",
#    packages=setuptools.find_packages(),
    install_requires=["cctk>=0.2.16"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
    ],
    python_requires='>=3.6',
)
