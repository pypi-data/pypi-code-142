from setuptools import setup

with open('README.md','r') as f:
    long_description = f.read()

setup(
    name="mytypo",
    version="0.0.1",
    description="Checks typos in one lines comments",
    url='https://github.com/worthrd/mytypo',
    author='Recep Daban',
    author_email='recep.daban@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["mytypo"],
    package_dir={'':'src'},
    entry_points={ 
        'console_scripts': [
            'mytypo = mytypo:check_typo'
        ]
    },
    install_requires = [
        'regex>=2022.10.31',
        'textblob>=0.17.1',
        'colorama>=0.4.6'
    ],
    extras_require = {
        "dev" : [
            "pytest>=7.2.0"
        ]
    },
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        "Topic :: Text Processing :: Linguistic",
        "Operating System :: OS Independent"
    ),
    keywords=["textblob", "nlp", 'linguistics', 'nltk', 'pattern']
    
)