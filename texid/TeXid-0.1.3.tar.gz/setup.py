import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='TeXid',
    packages=['TeXid'],
    version='0.1.3',
    description='Tense Identification using HuggingFace RoBERTa',
    author='Le Minh Khoi',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    py_modules=["TeXid"],
    install_requires=[]
)