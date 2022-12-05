from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='jupyter-duckdb',
    version='0.3',
    author='Eric Tröbs',
    author_email='eric.troebs@tu-ilmenau.de',
    description='a basic wrapper kernel for DuckDB',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erictroebs/jupyter-duckdb',
    project_urls={
        'Bug Tracker': 'https://github.com/erictroebs/jupyter-duckdb/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
        'jupyter',
        'duckdb~=0.6.0'
    ],
    package_data={
        'duckdb_kernel': ['kernel.json']
    },
    include_package_data=True,
)
