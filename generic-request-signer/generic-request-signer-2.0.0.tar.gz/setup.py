from setuptools import setup, find_packages

setup(
    name='generic-request-signer',
    version='2.0.0',
    author='imtapps',
    url='https://github.com/imtapps/generic-request-signer',
    description="A python library for signing http requests.",
    long_description=open('README', 'r').read(),
    install_requires=open('requirements/dist.txt', 'r').readlines(),
    packages=find_packages(exclude=("example", "request_signer.tests")),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
