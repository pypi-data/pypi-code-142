from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()
setup(
   name='choice_sort_pack',
   version='1.1',
   description='Модуль, проводящий сортировку выбором',
   long_description=long_description,
   license='MIT',
   packages=[
    'choice_sort_pack',
    ],
   install_requires=[
    'pytest',
    'argparse'
    ],
)
