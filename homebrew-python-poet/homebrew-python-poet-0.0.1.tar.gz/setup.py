from setuptools import setup

versionfile = 'poet/version.py'
with open(versionfile, 'rb') as f:
    exec(compile(f.read(), versionfile, 'exec'))

setup(
    name='homebrew-python-poet',
    version=__version__,  # noqa
    url='https://github.com/tdsmith/homebrew-pypi-poet',
    license='MIT',
    author='Justin S. Rice',
    author_email='justin@cloudhippie.com',
    description='Writes Homebrew formulae for Python packages',
    packages=['poet'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['jinja2', 'setuptools'],
    entry_points={'console_scripts': [
        'poet=poet:main',
        'poet_lint=poet.lint:main',
    ]}
)
