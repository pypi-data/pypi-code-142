from setuptools import setup, find_packages


setup(
    name='cotiwallet',
    version='0.0.1b',
    license='MIT',
    author="coti team",
    author_email='support@coti.io',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/coti-io/coti-sdk-python',
    keywords='example project',
    install_requires=[
          'urllib3', 'ecdsa', 'pycryptodome'
      ],

)