from setuptools import setup
from setuptools import find_packages

setup(
    name='celebrities_learning_test', #This will be the name your package will be published with
    version='0.0.1',
    description='Mock package that allows you to find a celebrty by date of birth',
    url='https://github.com/IvanYingX/project_structure-pypi.git', # Add the URL of your github repo if published
    author='Ivan Ying', # Your name
    license='MIT',
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4'] # All external libraries
)