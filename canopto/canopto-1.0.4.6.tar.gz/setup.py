from setuptools import setup, find_packages

requirements = [
    'aiofiles==22.1.0',
    'anyio==3.6.2',
    'beautifulsoup4==4.11.1',
    'certifi==2022.9.24',
    'cffi==1.15.1',
    'cryptography==38.0.3',
    'h11==0.14.0',
    'h2==4.1.0',
    'hpack==4.0.0',
    'httpcore==0.16.1',
    'httpx==0.23.1',
    'hyperframe==6.0.1',
    'idna==3.4',
    'importlib-metadata==5.0.0',
    'jaraco.classes==3.2.3',
    'jeepney==0.8.0',
    'keyring==23.11.0',
    'more-itertools==9.0.0',
    'prompt-toolkit==3.0.32',
    'pycparser==2.21',
    'rfc3986==1.5.0',
    'SecretStorage==3.3.3',
    'sniffio==1.3.0',
    'soupsieve==2.3.2.post1',
    'wcwidth==0.2.5',
    'zipp==3.10.0',
]

setup(
    name='canopto',
    version='1.0.4.6',
    author='Atticus T',
    author_email='theresurgence2@proton.me',
    url="https://github.com/theresurgence/canopto",
    description="canopto is a tool to sync course files and videos from the Canvas LMS hosted by the National University of Singapore(NUS).",
    license='GPLv3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'canopto=canopto.__main__:cli'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords='canopto canvas panopto nus',
    install_requires=requirements,
    zip_safe=False
)

print(find_packages())
# packages=find_packages(),
