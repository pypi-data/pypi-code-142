# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lattice', 'lattice.docs']

package_data = \
{'': ['*'],
 'lattice.docs': ['hugo_layouts/landing/*',
                  'hugo_layouts/partials/*',
                  'hugo_layouts/specifications/*']}

install_requires = \
['GitPython==3.1.18',
 'Jinja2',
 'cbor2',
 'jsonschema',
 'pyyaml',
 'stringcase==1.2.0']

setup_kwargs = {
    'name': 'lattice',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Big Ladder Software',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
