from setuptools import setup
from wsblib import __version__

with open('README.md', 'r') as reader:
    readme = reader.read()

setup(
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    name='wsblib',
    version=__version__,
    description='Base library for other web servers.',
    long_description_content_type='text/markdown',
    long_description=readme,
    packages=['wsblib'],
    install_requires=['http_pyparser==0.4.1'],
    url='https://github.com/firlast/wsblib',
    keywords=['www', 'http', 'server', 'internet', 'socket'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI'
    ],
    project_urls={
        'License': 'https://github.com/firlast/wsblib/blob/master/LICENSE'
    }
)