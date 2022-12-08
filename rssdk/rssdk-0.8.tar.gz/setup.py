import os
# Always prefer setuptools over distutils
from setuptools import setup, Extension

from Cython.Build import cythonize

package_data = {'rssdk': ['*.py', '*.pyi', 'py.typed']}
if os.name == 'nt':
    package_data['rssdk'].append('*.dll')

rsdio_sources = [
    'src/rssdk/rsdio/rsdio.pyx',
    "SDK/dio/src/rsdioimpl.cpp",
    "SDK/dio/src/controllers/ite8783.cpp",
    "SDK/dio/src/controllers/ite8786.cpp",
    "SDK/utils/tinyxml2.cpp",
    "SDK/error/src/rserrors.cpp"
]

rspoe_sources = [
    'src/rssdk/rspoe/rspoe.pyx',
    "SDK/poe/src/rspoeimpl.cpp",
    "SDK/poe/src/controllers/pd69104.cpp",
    "SDK/poe/src/controllers/pd69200.cpp",
    "SDK/poe/src/controllers/ltc4266.cpp",
    "SDK/utils/tinyxml2.cpp",
    "SDK/utils/i801_smbus.cpp",
    "SDK/error/src/rserrors.cpp"
]

rsdio_extension = Extension(
    'rssdk.rsdio',
    language='c++',
    sources=rsdio_sources,
    include_dirs=['exports', 'SDK/dio/include', 'SDK/utils'],
    extra_compile_args=['-DRSDIO_VERSION_STRING="3.0.4"']
)

rspoe_extension = Extension(
    'rssdk.rspoe',
    language='c++',
    sources=rspoe_sources,
    include_dirs=['exports', 'SDK/poe/include', 'SDK/utils'],
    extra_compile_args=['-DRSPOE_VERSION_STRING="3.0.5"']
)

setup(
    package_dir={"": "src"},
    packages=['rssdk'],
    ext_modules=cythonize(
        [rsdio_extension, rspoe_extension],
        language_level='3',
        compiler_directives={"linetrace": True} # Opt-in via CYTHON_TRACE macro
    ),
    setup_requires=[
        'cython >= 0.22.1',
    ],
    include_package_data=False,
    package_data=package_data,
    zip_safe=False,
)
