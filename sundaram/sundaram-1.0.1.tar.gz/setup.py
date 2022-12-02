from os import path
from setuptools import setup

try:
    current_path = path.abspath(path.dirname(__file__))
except NameError:
    current_path = None
try:
    with open(path.join(current_path, 'README.md'),
              encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''
setup(
    name='sundaram',
    version='1.0.1',
    # list folders, not files
    packages=['sundaram',
              'sundaram.test'],
    scripts=['sundaram/bin/sundaram_script.py',
             'sundaram/test/test_sundaram.py'],
    license='MIT License',
    description='Расчет решета сундарама',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
