import os
import sys

from setuptools import setup, Extension

sys.path.insert(0, os.path.join(os.getcwd(), "sepl_light_lib"))

from pkginfo import __author__, __version__

setup(
    name="sepl-light-lib",
    version=__version__,
    author=__author__,
    description="Library for convenient work with interference phenomena",
    url="https://github.com/Sersoid/SEPL-Light-Lib",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],
    ext_modules=[
        Extension(
            name="_sepl_light_lib",
            sources=[
                "src/extension.c",
                "src/wave/wave_module.c",
                "src/wave/components/cie_rgb.c"
            ],
            depends=[
                "src/wave/wave_module.h",
                "src/wave/components/cie_rgb.h"
            ],
            include_dirs=[
                "src/wave",
                "src/wave/components"
            ],
            define_macros=[
                ('SEPLLIGHTLIB_VERSION', __version__),
                ('SEPLLIGHTLIB_AUTHOR', __author__)
            ]
        )
    ],
    packages=[
        "sepl_light_lib"
    ],
    include_package_data=True,
    zip_safe=False
)
