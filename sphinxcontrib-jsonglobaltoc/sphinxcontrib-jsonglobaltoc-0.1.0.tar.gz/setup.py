from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="sphinxcontrib-jsonglobaltoc",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sphinx",
        "sphinxcontrib-serializinghtml"
    ],
    author="Caltech IMSS ADS",
    author_email="cmalek@caltech.edu",
    url="https://github.com/caltechads/sphinxcontrib-jsonglobaltoc",
    description="Sphinx extension to add a global table of contents to JSON output files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['documentation', 'sphinx', 'json'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
