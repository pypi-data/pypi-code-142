from setuptools import setup

readme = open(".\README.md", "r")

setup(
    name='elapsed_time',
    version='1.1',
    description='Measure exec time of a Python function',
    long_description=readme.read(),
    long_description_content_type="text/markdown",
    author='Esteban Osorio',
    author_email='estebandmp17@gmail.com',
    url='https://github.com/Estebandotpy/elapsed_time',
    keywords=['testing', 'example'],
    classifiers=[],
    license='MIT',
    include_package_data=True
)