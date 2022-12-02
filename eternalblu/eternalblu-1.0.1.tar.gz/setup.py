from setuptools import setup

setup(
    name='eternalblu',
    version='1.0.1',
    description='Eternal Blu Python package',
    url='https://github.com/boopathyganesh/kraken',
    author='Kraken Rogers',
    author_email='kraken@gmail.com',
    license='Apache Software License',
    packages=['eternalblu'],
    install_requires=['pandas',
                      'numpy', 'matplotlib','scikit-learn'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10'
    ],
)