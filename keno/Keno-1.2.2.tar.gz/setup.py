from setuptools import setup

setup(
    name='Keno',
    version='1.2.2',
    description='A Keno Game for Python',
    url='https://github.com/Xtarii/KenoPython',
    author='Lord Alvin Hansen',
    author_email='alvin.hansen@elev.ga.ntig.se',
    license='BSD 2-clause',
    packages=['keno'],
    install_requires=['styles>=0.1.5'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)