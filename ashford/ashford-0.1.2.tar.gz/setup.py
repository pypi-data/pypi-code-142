# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ashford']

package_data = \
{'': ['*']}

install_requires = \
['camina>=0.1.10,<0.2.0', 'miller>=0.1.6,<0.2.0']

setup_kwargs = {
    'name': 'ashford',
    'version': '0.1.2',
    'description': 'factory, registration, and validation tools for python',
    'long_description': '[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![PyPI Latest Release](https://img.shields.io/pypi/v/ashford.svg)](https://pypi.org/project/ashford/) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Documentation Status](https://readthedocs.org/projects/ashford/badge/?version=latest)](http://ashford.readthedocs.io/?badge=latest)\n\n\n\n\n# Why ashford?\n\nThis package provides classes and decorators for a variety of Python implementations of registration, factories, and type validators.\n\n<p align="center">\n<img src="https://media.giphy.com/media/Fl7aszvRTsJhsAfyG2/giphy.gif" height="300"/>\n</p>\n\n\n## Registries\n<p align="center">\n<img src="https://media.giphy.com/media/tWY3sKzNDpwgzKwzMa/giphy.gif" height="300"/>\n</p>\n\n* `registered`: a decorator that stores a registry in a `registry` attribute of the function or class which is wrapped by the decorator.\n* `Registrar`: a mixin for automatic subclass registration.\n\n\n## Factories\n<p align="center">\n<img src="https://media.giphy.com/media/pKEF7XmUlRGFayOyLJ/giphy.gif" height="300"/>\n</p>\n* `InstanceFactory`: mixin that stores all subclass instances in the `instances` class attribute and returns stored instances when the `create` classmethod is called.\n* `LibraryFactory`: mixin that stores all subclasses and subclass instances in the `library` class attribute and returns stored subclasses and/or instances when the `create` classmethod is called.\n* `SourceFactory`: mixin that calls the appropriate creation method based on the type of passed first argument to `create` and the types stored in the keys of the `sources` class attribute.\n* `StealthFactory`: mixin that returns stored subclasses when the `create` classmethod is called without having a `subclasses` class attribute like SubclassFactory.\n* `SubclassFactory`: mixin that stores all subclasses in the `subclasses` class attribute and returns stored subclasses when the `create` classmethod is called.\n* `TypeFactory`: mixin that calls the appropriate creation method based on the type of passed first argument to `create` and the snakecase name of the type. This factory is prone to significant key errors unless you are sure of the snakecase names of all possible submitted type names. SourceFactory avoids this problem by allowing you to declare corresponding types and string names.\n\n## Validators\n\n\n<p align="center">\n<img src="https://media.giphy.com/media/emN3Lsx8elioidwcLS/giphy.gif" height="300"/>\n</p>\n\n\n* `bonafide`: decorator that validates or converts types based on type annotations of the wrapped function or dataclass (under construction)\n* \nashford`s framework supports a wide range of coding styles. You can create complex multiple inheritance structures with mixins galore or simpler, compositional objects. Even though the data structures are necessarily object-oriented, all of the tools to modify them are also available as functions, for those who prefer a more funcitonal approaching to programming. \n\nThe project is also highly internally documented so that users and developers can easily make ashford work with their projects. It is designed for Python coders at all levels. Beginners should be able to follow the readable code and internal documentation to understand how it works. More advanced users should find complex and tricky problems addressed through efficient code.',
    'author': 'corey rayburn yung',
    'author_email': 'coreyrayburnyung@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/WithPrecedent/ashford',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
