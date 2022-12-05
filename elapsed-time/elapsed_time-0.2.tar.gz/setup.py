from setuptools import setup

readme = open(".\README.md", "r")

setup(
    name='elapsed_time',
    version='0.2',
    description='Measure time of excec',
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