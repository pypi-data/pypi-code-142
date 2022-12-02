from setuptools import setup

setup(
    name='listkraken',
    version='0.1.0',    
    description='Kraken Python package',
    url='https://github.com/boopathyganesh/kraken',
    author='Kraken Rogers',
    author_email='kraken@gmail.com',
    license='Apache Software License',
    packages=['listkraken'],
    install_requires=['pandas',
                      'numpy',                     
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