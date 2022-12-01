from pathlib import Path
from setuptools import find_packages, setup
dependencies = []

setup(
    name='orderflow',
    packages=find_packages(),
    version='0.0.1',
    description='',
    author='Alireza Roosta',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=dependencies,
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest==4.4.1'],
    # test_suite='tests',
)
