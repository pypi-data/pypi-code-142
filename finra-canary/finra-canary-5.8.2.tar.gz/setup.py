from setuptools import setup, find_packages

setup(
    name='finra-canary',
    version='5.8.2',
    license='MIT',
    author="Shubham_fnra",
    author_email='shubham.agrawal@finra.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='ceedee project',
    install_requires=[
          'scikit-learn',
          'requests',
      ],
)
