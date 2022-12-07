from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='xPDF50',
    version='0.0.5',
    description='Get clean PDFs of CS50 course materials from thier URLs',
    long_description = long_description, long_description_content_type=("text/markdown"),
    py_modules=["xPDF50"],
    # package_dir={'':'src'},
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'xPDF50 = xPDF50.xPDF50:main'
        ]
    },
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require = {
            "dev": [
                "pytest>=3.7",
            ],
    },
    url="https://github.com/thaare87/projects/tree/master/xPDF50",
    author="Thaare87",
    author_email="thaare87@gmail.com",
)

