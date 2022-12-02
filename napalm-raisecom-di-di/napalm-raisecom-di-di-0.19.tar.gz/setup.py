from setuptools import find_packages, setup

list_packages = ['napalm', 'netmiko']

setup(
    name='napalm-raisecom-di-di',
    version='0.19',
    description='driver napalm functionality for raisecom devices, via netmiko connection',
    url='',
    author='Ilya Gulin',
    license='Apache 2.0',
    install_requires=[*list_packages],
    packages=find_packages(),
    include_package_data=True,
)
