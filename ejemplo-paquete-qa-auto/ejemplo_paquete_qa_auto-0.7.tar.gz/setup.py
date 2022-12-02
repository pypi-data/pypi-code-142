from setuptools import setup, find_packages


setup(
    name='ejemplo_paquete_qa_auto',
    version='0.7',
    license='MIT',
    author="Giorgos Myrianthous",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project new',
    install_requires=[
          'scikit-learn',
      ],

)
