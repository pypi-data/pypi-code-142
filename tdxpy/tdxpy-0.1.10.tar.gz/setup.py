#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

cython_deps = ["cython", ]
ext_modules = {}

# try:
#     from Cython.Build import cythonize
#
#     ext_modules = {
#         "ext_modules": cythonize(
#             [
#                 "tdxpy/parser/std/get_security_quotes.py",
#                 "tdxpy/base_socket_client.py",
#                 "tdxpy/parser/base.py",
#                 "tdxpy/helper.py",
#                 "tdxpy/hq.py",
#             ]
#         )
#     }
#
# except ImportError:
#     pass

try:
    import pypandoc

    long_description = pypandoc.convert_file('README.md', 'rst')
except (IOError, ImportError):
    print(30 * "*")
    print("Notice, NEED TO INSTALL *pypandoc* TO get full description of package")
    print(30 * "*")
    long_description = ''
    exit()

setup(
    name="tdxpy",
    version="0.1.10",
    description="TDXPY - Python TDX 数据接口",
    long_description=long_description,
    maintainer="BoPo",
    maintainer_email="ibopo@126.com",
    url="https://github.com/mootdx/tdxpy",
    packages=find_packages(include=["tdxpy", "tdxpy.*"]),
    # include_package_data=True,
    install_requires=["cryptography", "pandas"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    # extras_require={
    #     # can be installed by pip install modin[dask]
    #     "cython": cython_deps,
    # },
    # **ext_modules,
)
