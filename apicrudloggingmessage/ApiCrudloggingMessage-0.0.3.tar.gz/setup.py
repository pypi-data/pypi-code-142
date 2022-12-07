from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ApiCrudloggingMessage',
  version='0.0.3',
  description='Its the Api logging message for crud operations ',
#   long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Vijayakumar Kanniah',
  author_email='x21188955@student.ncirl.ie',
#   license='MIT', 
  classifiers=classifiers,
  keywords='logging', 
  packages=find_packages(),
  install_requires=[''] 
)