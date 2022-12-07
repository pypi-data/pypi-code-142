# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autodisco']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2,<5.0']

setup_kwargs = {
    'name': 'django-autodisco',
    'version': '0.1.0',
    'description': 'Django autodiscover modules utils',
    'long_description': '# django-autodisco\n\nMicro django lib that helps auto-loading app modules.\n\n**Why this lib?**\n\nI am used to grouping signal connectors and receivers in a module called `receivers.py`. I didn\'t want add the module import in the `ready` method of all the apps anymore.\n\n---\n\n## Installation\n\n```bash\npython -m pip install \'django-autodisco @ git+https://github.com/etchegom/django-autodisco.git\'\n```\n\n---\n\n## Usage\n\nAdd the `autodisco` django app:\n\n```python\nINSTALLED_APPS = [\n    ...\n    "autodisco",\n]\n```\n\nDefine the modules to auto-load in settings:\n\n```python\n\nAUTODISCO_MODULES = [\n    "receivers",\n    ...\n]\n\n```\n\n---\n\n## Run example\n\n```bash\nmake example\n```\n\n---\n\n## Run tests\n\n```bash\nmake tests\n```\n',
    'author': 'Matthieu Etchegoyen',
    'author_email': 'etchegom@gmail.com',
    'maintainer': 'Matthieu Etchegoyen',
    'maintainer_email': 'etchegom@gmail.com',
    'url': 'https://github.com/etchegom/django-fsm-admin-lite',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
