#!/usr/bin/python

from setuptools import (
    setup,
    find_packages
    )

requires: list = ["requests", "urllib3", "datetime", "rubx"]
version: str = '1.0.0'
readme: str = (
    """

#Rubika

    """
    )

setup(
    name="robika",
    version=version,
    description="rubika client handler",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="SaJad",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    keywords=[
        'rubika',
        'telegram',
        'rubx',
        'telethon',
        'pyrogram',
        'rubikaClient',
        'rubika-bot',
        'telegram-bot'
        ],
    python_requires="~=3.5",
    packages=find_packages(),
    zip_safe=False,
    install_requires=requires
)