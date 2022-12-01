from setuptools import setup, find_packages

setup(
    name='lognwrite',
    version='0.1.1',
    license='MIT',
    author="Muhammad Alif Putra Yasa",
    author_email='malifputrayasa@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/malifpy/log-n-write',
    keywords='log',
    readme= 'README.md',
    install_requires=[
        'typing_extensions',
    ],
)
