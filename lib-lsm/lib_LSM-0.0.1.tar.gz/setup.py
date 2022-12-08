from setuptools import setup, find_packages
classifiers = [ 
   'Development Status :: 5 - Production/Stable',
   'Intended Audience : : Education',
   'Operating System :: OS independant',
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3'
]
setup(
  name='lib_LSM',
  version='0.0.1',
  description= 'Issue books and calculate fine',
  Long_descriptionsopen= open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Pushkar Rahane',
  author_email= 'p.rahane210@gmail.com',
  License='MIT',
  cLassifiers=classifiers,
  keywords='issue book',
  packages=find_packages(),
  install_requires=['']
)  