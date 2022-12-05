from setuptools import setup

setup(
    name='sphinx-mathjax-offline',
    version='0.0.2',
    url='https://gitlab.com/thomaswucher/sphinx-mathjax-offline',
    license='Apache License 2.0',
    author='Thomas Wucher',
    author_email='mail@thomaswucher.de',
    description='MathJax offline support for Sphinx',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx-mathjax-offline'],
    package_data={'sphinx-mathjax-offline': [
        'static/mathjax/*',
        'static/mathjax/*/*',
        'static/mathjax/*/*/*',
        'static/mathjax/*/*/*/*',
        'static/mathjax/*/*/*/*/*',
    ]},
    include_package_data=True,
    install_requires=[
        'sphinx'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
