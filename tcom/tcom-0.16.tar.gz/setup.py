# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tcom']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=3.0', 'markupsafe>=2.0', 'whitenoise>=5.3']

setup_kwargs = {
    'name': 'tcom',
    'version': '0.16',
    'description': 'Replace your HTML templates with Python server-Side components',
    'long_description': '<h1>\n  <img\n    src="https://github.com/jpsca/tcom/raw/main/docs/assets/images/logo.png"\n    width="48" height="48"\n    align="bottom"\n   >\n  Template Components\n</h1>\n\nThe power of components in your server-side-rendered Python web app.\n\n**Documentation:** https://tcom.scaletti.dev/\n\nWrite server-side components as single Jinja template files.\nUse them as HTML tags without doing any importing.\n\n<img class="card-code"  src="./docs/assets/images/card-code.png" height="300">\n\n## About\n\nThis project is developed by *Juan-Pablo Scaletti*.<br>\nI love building products and sharing knowledge.\n\n',
    'author': 'Juan-Pablo Scaletti',
    'author_email': 'juanpablo@jpscaletti.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://tcom.scaletti.dev/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
