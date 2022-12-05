from setuptools import setup, find_packages


setup(
    name='d-typewriter',
    version='0.3',
    license='MIT',
    author="Drooler",
    author_email='contact@drooler.tk',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/drooler/typewriter',
    keywords='typewriter python',
    install_requires=[
          'scikit-learn',
      ],

)