from setuptools import setup, find_packages
import random

VERSION = '0.0.11'
DESCRIPTION = 'add, roll, lustig'


# Setting up
setup(
    name="allesLib",
    version=VERSION,
    author="HomeCamper",
    author_email="<huber.xittam@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)