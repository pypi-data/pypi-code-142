from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='basicutilspackage',
  version='0.0.1',
  description='A very basic packages',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='pbl6-group2',
  author_email='joblink.pbl6@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='utils', 
  packages=find_packages(),
  install_requires=[''] 
)
