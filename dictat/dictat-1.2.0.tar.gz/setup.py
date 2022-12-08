import shlex
import subprocess

import setuptools

try:
    git_version = subprocess.check_output(
        shlex.split('git describe --tags --always')
    ).decode().strip()
except subprocess.CalledProcessError:
    git_version = 'v0.0.0'


setuptools.setup(
    name='dictat',
    version=git_version,
    description='Adict is an attribute-accessible dynamic dictionary wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Janos Kutscherauer',
    author_email='janoskut@gmail.com',
    url='https://gitlab.com/janoskut/dictat',
    license='UNLICENSE',
    license_files = ['UNLICENSE'],
    packages=['dictat'],
    install_requires=[],
    python_requires='>=3.7',
    package_data={'dictat': ['dictat/py.typed']},
    include_package_data=True,
)
