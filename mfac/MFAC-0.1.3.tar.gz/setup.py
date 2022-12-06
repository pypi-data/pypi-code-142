import os
from distutils.core import setup

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='MFAC',
    packages=['MFAC'],
    version='0.1.3',
    license='GPLv3',
    description='Model Free Adaptive Control',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Shahin Darvishpoor',
    author_email='Shahindarvishpoor@gmail.com',
    url='https://github.com/shahind/MFAC',
    download_url='https://github.com/shahind/MFAC/releases/download/MFAC-0.1.3/MFAC-0.1.3.tar.gz',
    keywords=['MFAC', 'Control', 'Dynamic'],
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
