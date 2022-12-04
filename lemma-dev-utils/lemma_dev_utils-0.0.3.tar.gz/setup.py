from setuptools import setup, find_packages

setup(
    name='lemma_dev_utils',
    version='0.0.3',
    license='MIT',
    author="Ludovico Lemma",
    author_email='lwdovico@protonmail.com',
    packages=find_packages('source'),
    package_dir={'': 'source'},
    url='https://github.com/ludovicolemma/lemma-dev-utils',
    keywords='Utils',
    install_requires=[
          'tqdm',
          'imageio',
      ],

)