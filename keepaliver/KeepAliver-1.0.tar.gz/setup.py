from setuptools import setup, find_packages
 
setup(
    name='KeepAliver',
    version='1.0',
    license='MIT', 
    keywords='keepalive', 
    packages=find_packages(),
    install_requires=['colorama', 'flask'] 
)