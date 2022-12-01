from setuptools import setup

setup(
   name='PyAdvDocx',
   version='0.0.1',
   author='SerbanTudor04',
   author_email='tudor.gabriel.serban@gmail.com',
   packages=['pyadvdocx',],
   scripts=[],
   url='https://github.com/SerbanTudor04/PyAdvDocx/',
   license='LICENSE',
   description='An open source project inspired from python-docx .',
   long_description=open('README.md').read(),
   install_requires=[
       "python-docx",
   ],
)