# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['springdata', 'springdata.asyncio', 'springdata.domain']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'spring-data-python',
    'version': '0.1.6',
    'description': 'Spring Data Python is an offshoot of the Java-based Spring Data Framework, targeted for Python.',
    'long_description': '# spring-data-python\nSpring Data Python is an offshoot of the Java-based Spring Data Framework, targeted for Python. \n',
    'author': 'Vincent TERESE',
    'author_email': 'vincent.terese@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kobibleu/spring-data-python',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
