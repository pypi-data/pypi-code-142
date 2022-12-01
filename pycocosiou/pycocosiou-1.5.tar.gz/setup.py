"""To compile and install locally run "python setup.py build_ext --inplace".
To install library to Python site-packages run "python -m pip install --use-feature=in-tree-build ."
"""
import platform
from setuptools import setup, Extension

import numpy as np

ext_modules = [
        Extension(
            'pycocosiou._mask',
            sources=['./common/maskApi.c', 'pycocosiou/_mask.pyx'],
            include_dirs=[np.get_include(), './common'],
            extra_compile_args=[] if platform.system()=='Windows' else
            ['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
        )
    ]

setup(
    name='pycocosiou',
    description='Unofficial APIs for the MS-COCO dataset with SIOU evaluation',
    url="https://github.com/pierlj/extended_pycocotools",
    license="FreeBSD",
    packages=['pycocosiou'],
    package_dir={'pycocosiou': 'pycocosiou'},
    python_requires='>=3.5',
    install_requires=[
        'matplotlib>=2.1.0',
        'numpy',
    ],
    version='1.5',
    ext_modules=ext_modules
)