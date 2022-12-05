from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Intended Audience :: Education',
  'Intended Audience :: Information Technology',
  'Operating System :: Microsoft :: Windows :: Windows 10 ',
  'Operating System :: Microsoft :: Windows :: Windows 11 ',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='LAPCA',
  version='0.0.2',
  description='LAPCA is a tool that is used to check whether the given program conforms to the specified guidelines. ',
  long_description_content_type="text/markdown",
  long_description=open('README.md').read() + '\n\n',
  url='',  
  author='Swaroop Bhat',
  author_email='swaroopbhat510@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['Conformance','language agnostic','program','guidelines','LAPCA','LAPCA Score'], 
  packages=find_packages(),
  install_requires=[''] 
)
