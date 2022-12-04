#!/usr/bin/env python3
from setuptools import setup

setup(
    name="speedport-api",
    description="Control Telekom Speedport routers with Python",
    version="0.1.0",
    author="Andre Basche",
    license="MIT",
    url="https://github.com/Andre0512/speedport-api",
    platforms="any",
    py_modules=["jeelink-python"],
    package_dir={"": "src"},
    packages=["speedport-api"],
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["requests", "pycryptodome"],
    entry_points={
        'console_scripts': [
            'speedport = speedport_api.__main__:main',
        ]
    }
)
