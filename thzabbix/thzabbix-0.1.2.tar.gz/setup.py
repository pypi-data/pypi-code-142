from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='thzabbix',
    version='0.1.2',
    packages=['thzabbix'],
    url='https://github.com/thorvaldhrafn/thzabbix',
    license='MIT License',
    author='Volodymyr Borysiuk',
    author_email='thorvaldr.hrafn@gmail.com',
    description='Package for work with zabbix api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
