from setuptools import setup

setup(
    name='StringSort',
    packages=['StringSort'],
    version='9.0.0',
    license='MIT',
    description='string sorting library',
    author='Luka',
    author_email='app6onpython@gmail.com',
    keywords=['sort', 'string', 'StringSort', 'string sort', 'String Sort',
              'string_sort', 'String_sort', 'String sort', 'Sort',
              'String'],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)

# python setup.py sdist
# twine upload --skip-existing dist/*