from setuptools import setup, find_packages

VERSION = '0.0.0'
DESCRIPTION = 'aplabcolemen'
LONG_DESCRIPTION = 'aplabcolemen'

# Setting up
setup(
    name="aplabcolemen",
    version=VERSION,
    author="Colemen Atwood",
    author_email="<atwoodcolemen@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    py_modules=[],
    # add any additional packages that
    # need to be installed along with your package. Eg: 'caer'
    install_requires=[
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
