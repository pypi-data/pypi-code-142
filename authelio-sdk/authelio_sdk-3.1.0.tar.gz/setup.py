from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

setup(
    name='authelio_sdk',
    version=VERSION,
    license='Apache License 2.0',
    packages=find_packages(exclude=[
        'venv',
        '.venv',
        'authelio_sdk_tests',
    ]),
    description=f'Authelio Python SDK',
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'b_lambda_layer_common>=4.2.2,<5.0.0',
        'urllib3>=1.26.0,<2.0.0'
    ],
    author='Gediminas Kazlauskas',
    author_email='gediminas.kazlauskas@biomapas.com',
    keywords='Authelio Python SDK',
    url='https://github.com/Biomapas/AuthelioPythonSDK.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
