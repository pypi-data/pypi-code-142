from setuptools import setup

setup(
   name='df_data_validator',
   version='0.0.1',
   description='Data Validation package',
   author='Shrishty',
   packages=['df_data_validator'],  #same as name
   install_requires=['pandas', 'datatest','datetime'], #external packages as dependencies
)

