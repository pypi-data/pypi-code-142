#!/usr/bin/env python
import ast
import codecs
import os
import re
from setuptools import find_packages, setup

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))
init = os.path.join(ROOT, 'src', 'smart_logging', '__init__.py')

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open(init, 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

requirements = ["redis",
                "django-smart-admin[full]"
                ]
tests_require = ["django-webtest",
                 "flake8",
                 "isort",
                 "pytest",
                 "pytest-coverage",
                 "pytest-django",
                 "pytest-echo",
                 "redis",
                 "tox",
                 ]
dev_require = ["pdbpp",
               "black",
               "django_smart_admin",
               "django"]
docs_require = []

setup(
    name='django-smart-logging',
    version=version,
    url='https://gitlab.com/os4d/django-smart-logging.git',
    download_url='https://gitlab.com/os4d/django-smart-logging',
    author='sax',
    author_email='s.apostolico@gmail.com',
    description="",
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=requirements,
    tests_require=tests_require,
    extras_require={
        'test': requirements + tests_require,
        'dev': dev_require + tests_require,
        'docs': dev_require + docs_require,
    },
    zip_safe=False,
    platforms=['any'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
