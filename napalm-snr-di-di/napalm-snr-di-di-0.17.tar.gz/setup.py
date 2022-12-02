from setuptools import find_packages, setup

list_packages = ['napalm', 'netmiko']

setup(
    name='napalm-snr-di-di',
    version='0.17',
    description='driver napalm functionality for snr devices, via netmiko connection',
    url='',
    author='Ilya Gulin',
    license='Apache 2.0',
    install_requires=[*list_packages],
    packages=find_packages(),
    include_package_data=True,
)
