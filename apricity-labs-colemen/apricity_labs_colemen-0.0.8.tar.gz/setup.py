
# import colemen_utils as _c
import build_utils as _bu
from setuptools import setup, find_packages

VERSION = '0.0.8'
DESCRIPTION = 'apricity_labs_colemen'
LONG_DESCRIPTION = 'apricity_labs_colemen'

PY_MODULES = _bu.list_py_modules()

_bu.purge_dist()

# Setting up
setup(
    name="apricity_labs_colemen",
    version=VERSION,
    author="Colemen Atwood",
    author_email="<atwoodcolemen@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    py_modules=[
        'apricity_labs'] + PY_MODULES,
    # add any additional packages that
    # need to be installed along with your package. Eg: 'caer'
    install_requires=[
        'colemen_utils',
        'flask',
        'pyjwt',
        'cerberus',
    ],

    keywords=['python'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
