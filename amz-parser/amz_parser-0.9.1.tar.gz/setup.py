from distutils.core import setup

setup(name='amz_parser',
      version='0.9.1',
      description='Extract useful data from Amazon pages.',
      author='lonely',
      packages=['amz_parser'],
      package_dir={'amz_parser': 'amz_parser'},
      install_requires=['dateparser>=1.1.4', 'pyquery>=1.4.3']
      )
