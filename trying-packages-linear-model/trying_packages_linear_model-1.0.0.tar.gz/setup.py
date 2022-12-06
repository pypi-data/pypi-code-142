from setuptools import setup

setup(
   name='trying_packages_linear_model',
   version='1.0.0',
   author='me',
   author_email='assia@gmail.com',
   packages=['linear_model'],
   url='http://pypi.python.org/pypi/linear_model/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   install_requires=['linear_model.py']
)