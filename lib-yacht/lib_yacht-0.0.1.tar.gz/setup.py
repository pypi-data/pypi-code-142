from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='lib_yacht',
  version='0.0.1',
  description='Email will be sent to the provided email ',
#   long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Stephen Angelo',
  author_email='x21220123@student.ncirl.ie',
#   license='MIT', 
  classifiers=classifiers,
  keywords='lib_yacht',
  packages=find_packages(),
  install_requires=[''] 
)