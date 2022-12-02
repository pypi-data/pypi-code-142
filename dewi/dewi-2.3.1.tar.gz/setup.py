#!/usr/bin/env python3
#
# DEWI: a developer tool and framework
# Copyright (C) 2012-2021  Laszlo Attila Toth
# Distributed under the terms of the GNU Lesser General Public License v3


import sys

if sys.hexversion < 0x030a0000:
    raise RuntimeError("Required python version: 3.10 or newer (current: %s)" % sys.version)

from setuptools import setup, find_packages

setup(
    name="dewi",
    description="DEWI - A toolchain and framework for everyday tasks",
    long_description=\
    """
    DEWI is started as a developer tool, but contains many different dewi_commands.commands (small tools).

    It is a meta package for the DEWI packages and provides a command-line
    application for the commands in dewi_commands package.
    """,
    license="LGPLv3",
    version="2.3.1",
    author="Laszlo Attila Toth",
    author_email="python-dewi@laszloattilatoth.me",
    maintainer="Laszlo Attila Toth",
    maintainer_email="python-dewi@laszloattilatoth.me",
    keywords='tool framework development synchronization',
    url="https://github.com/LA-Toth/dewi",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: System :: Filesystems',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
    zip_safe=True,
    use_2to3=False,
    python_requires='>=3.10',
    packages=find_packages(exclude=['pylintcheckers', '*test*']),
    entry_points={
        'console_scripts': [
            'dewi=dewi.__main__:main',
        ]
    },
    install_requires=[
        'dewi_core >=5.4.0, <6',
        'dewi_commands >=3.1.0, <4',
    ]
)
