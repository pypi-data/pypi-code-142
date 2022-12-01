# Copyright 2020-present, Mayo Clinic Department of Neurology
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


import setuptools
from glob import glob

from setuptools import Command, Extension
import shlex
import subprocess
import os
import re

## get version from file
VERSIONFILE="./ncs2mef/__init__.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))



setuptools.setup(
    name="ncs2mef",
    version=verstr,
    license='',
    url="https://github.com/mselair/ncs2mef",

    author="Filip Mivalt",
    author_email="mivalt.filip@mayo.edu",


    description="Custom made Python reader for Neuralynx Cheetah NCS files.",
    long_description="Custom made Python reader for binary NCS EEG files generated using Neuralynx Cheetah. Codes were inspired by publicly available codes at https://neuralynx.com/software/category/matlab-netcom-utilities.",
    long_description_content_type="",

    packages=setuptools.find_packages(),

    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Operating System :: POSIX :: Linux",
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    python_requires='>=3.6',
    install_requires =[
        'numpy',
    ]
)






