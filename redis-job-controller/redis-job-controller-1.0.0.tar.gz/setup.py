from setuptools import setup, find_packages
import os


version = os.getenv("PACKAGE_VERSION", "0.0.9a")


setup(
    name='redis-job-controller',
    version=version,
    description='Package for enqueuing and fetching async jobs, using Redis as a queue and result repository',
#    long_description=readme,
    author='Karol Ważny',
#    author_email='me@kennethreitz.com',
#    url='https://github.com/kennethreitz/samplemod',
#    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['redis']
)
