from setuptools import setup

setup(
   name='pipTutorial',
   version='1.0',
   description='A useful module',
   long_description='Tutorial',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['pipTutorial'],  #same as name
   install_requires=[
    'pandas', 
    'numpy', 
    'matplotlib'
    ]
)