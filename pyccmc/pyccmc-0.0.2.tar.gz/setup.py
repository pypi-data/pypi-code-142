from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyccmc',
    version='0.0.2',
    packages=['pyccmc'],
    install_requires=[
        'requests',
        'tqdm',
        'colorama',
        'fake_useragent',
        'browser_cookie3'
    ],
    url='https://tigabeatz.net',
    author='tigabeatz',
    author_email='tigabeatz@cccwi.de',
    description='Download from CC Mixter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    entry_points={
        'console_scripts': [
            'ccmclient=pyccmc.cli:main'
        ]
    },
)

