from setuptools import setup, find_packages


setup(
    name='Matyasproject',
    version='1.0.1',
    author="Matyas aka chip",
    author_email='mkrizek@dons.usfca.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/matyaskrizek/testy',
    keywords='example project',
    install_requires=[
        'scikit-learn',
        'meshtastic'
    ],

)