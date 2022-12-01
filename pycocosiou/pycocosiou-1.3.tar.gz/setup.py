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
    packages=['pycocosiou'],
    package_dir = {'pycocosiou': 'pycocosiou'},
    install_requires=[
        'matplotlib>=2.1.0',
        'numpy',
    ],
    python_requires='>=3.5',
    version='1.3',
    ext_modules= ext_modules
)
