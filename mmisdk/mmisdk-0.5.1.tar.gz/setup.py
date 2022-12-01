import sys

if not 'sdist' in sys.argv:
    sys.exit(
        '\n ✋✋✋✋✋✋✋✋'
        '\n 🛑 The package `mmisdk` has been renamed `metamask-institutional.sdk`, and is no longer maintained under the name `mmisdk`.'
        '\n ✅ Use instead https://pypi.org/project/metamask-institutional.sdk.'
        '\n ✋✋✋✋✋✋✋✋')

from setuptools import setup


setup(
    name='mmisdk',
    version='0.5.1',
    description='The package `mmisdk` has been renamed `metamask-institutional.sdk`, and is no longer maintained under the name `mmisdk`. Use instead https://pypi.org/project/metamask-institutional.sdk.',
    author='Xavier Brochard',
    author_email='xavier.brochard@consensys.net',
    url='https://pypi.org/project/metamask-institutional.sdk/',
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3 :: Only',
        # 'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
        'Topic :: Office/Business :: Financial'
    ],
    project_urls={
        'Documentation': 'https://consensys.gitlab.io/codefi/products/mmi/mmi-sdk-py/sdk-python/',
        # 'Changelog': 'https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py/-/blob/main/CHANGELOG.md',
        # 'Issue Tracker': 'https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py/-/issues',
    },
    keywords='python sdk custodian interact get create transaction',
    python_requires='>=3.6',
    install_requires=[
        'pydantic>=1.10.1',
        'requests>=2.28.1',
        'cachetools>=5.2.0',
    ],
    extras_require={
        "dev": [
            "bump2version==1.0.1",
            "check-manifest==0.48",
            "pytest==7.1.3",
            "twine==4.0.1",
            "tox==3.26.0",
            "python-dotenv==0.21.0"
        ]
    },
    setup_requires=[
        'pytest-runner',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'mmisdk = mmisdk.cli:main',
    #     ]
    # },
)
