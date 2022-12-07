
"""setup.py for bufsock."""

from distutils.core import setup

version = '1.00'

setup(
    name='bufsock',
    py_modules=[
        'bufsock',
        ],
    version=version,
    description='A buffered socket module',
    long_description='''
A module for doing socket I/O in a greatly simplified manner.
''',
    author='Daniel Richard Stromberg',
    author_email='strombrg@gmail.com',
    url='http://stromberg.dnsalias.org/~strombrg/bufsock',
    platforms='Cross platform',
    license='UCI (BSD-like)',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        ],
    )
