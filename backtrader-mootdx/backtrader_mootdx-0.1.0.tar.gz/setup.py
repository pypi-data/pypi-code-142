"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'backtrader',
    'mootdx',
]

test_requirements = ['pytest>=3', ]

setup(
    author="bopo",
    author_email='ibopo@126.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description='Python Boilerplate contains all the boilerplate you need to create a Python package.',
    install_requires=requirements,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='backtrader_mootdx',
    name='backtrader_mootdx',
    packages=find_packages(include=['backtrader_mootdx', 'backtrader_mootdx.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bopo/backtrader_mootdx',
    version='0.1.0',
    zip_safe=False,
)
