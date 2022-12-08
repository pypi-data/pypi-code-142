from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='duprem',
  version='0.0.1',
  description='remove duplicates from list',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Aditya Gadre',
  author_email='coderzdevs@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='duprem', 
  packages=find_packages(),
  install_requires=[''] 
)
