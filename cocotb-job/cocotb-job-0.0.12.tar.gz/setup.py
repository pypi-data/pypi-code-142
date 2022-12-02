from setuptools import setup, find_packages
import codecs
import os


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


long_desc = """
todo
"""


def read_install_requires():
    reqs = [
        'requests',
        'py3fdfsv2',
        'pypinyin',
        'redis',
        'tqdm'
    ]
    return reqs


setup(
    name='cocotb-job',
    version='0.0.12',
    description='todo',
    long_description=long_desc,
    author='Daniel Qian',
    author_email='909263817@qq.com',
    license='MIT',
    url='https://cocotb-job.pro',
    install_requires=read_install_requires(),
    keywords='todo',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.csv', '*.txt']},
)