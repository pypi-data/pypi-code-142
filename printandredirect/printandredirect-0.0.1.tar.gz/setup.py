from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='printandredirect',
  version='0.0.1',
  description='simple pageredirect function',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='madhanreddy',
  author_email='srimadhanreddy.1995@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='validateandgreet', 
  packages=find_packages(),
  install_requires=[''] 
)