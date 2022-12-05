from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='TempMailFB',
  version='0.0.1',
  description='This for testing',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='HearHour',
  author_email='hourfoto@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='tempmailfb',
  packages=find_packages(),
  install_requires=['']
)
