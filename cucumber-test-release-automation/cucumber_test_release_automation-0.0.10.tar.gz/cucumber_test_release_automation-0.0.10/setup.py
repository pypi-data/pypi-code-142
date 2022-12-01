# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cucumber_test_release_automation']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cucumber-test-release-automation',
    'version': '0.0.10',
    'description': '',
    'long_description': '',
    'author': 'Matt Wynne',
    'author_email': 'matt@cucumber.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
