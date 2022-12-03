from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='AdventOfCode2022',
    version='1.00',
    packages=['AdventOfCode2022'],
    url='https://github.com/GlobalCreativeApkDev/AdventOfCode2022',
    license='MIT',
    author='GlobalCreativeApkDev',
    author_email='globalcreativeapkdev2022@gmail.com',
    description='My Advent of Code solutions in Python. '
                'https://adventofcode.com/2022',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "AdventOfCode2022=AdventOfCode2022.runner:main",
        ]
    }
)
