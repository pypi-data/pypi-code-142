from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

long_description = 'Command line program to produce modified config.'

setup(
    name='okndecide',
    version='1.0.1',
    author='Zaw Lin Tun',
    author_email='zawlintun1511@gmail.com',
    url='https://github.com/jtur044/okndecide',
    description='OKN config file modifier',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache Software",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'okndecide = okndecide.okndecide:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='OKN related config modifier',
    install_requires=requirements,
    zip_safe=False
)
