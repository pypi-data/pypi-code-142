from setuptools import setup, find_packages


setup(
    name='torch_with_abi',
    version='1.11',
    license='MIT',
    author="Orene Elmaleh",
    author_email='orene_elmaleh@saips.co.il',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/orene-elmaleh/torch_with_abi',
    keywords='torch abi',
    install_requires=[
      ],
)
