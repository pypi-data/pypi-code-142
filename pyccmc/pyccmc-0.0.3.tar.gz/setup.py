from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyccmc',
    version='0.0.3',
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
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    entry_points={
        'console_scripts': [
            'ccmclient=pyccmc.cli:main'
        ]
    },
)

