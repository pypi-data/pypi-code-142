# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['st_lianshan',
 'st_lianshan.layout',
 'st_lianshan.module',
 'st_lianshan.module.compute',
 'st_lianshan.module.reports',
 'st_lianshan.module.templates']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.2',
 'python-decouple>=3.6,<4.0',
 'python-dotenv>=0.19.1,<0.20.0',
 'simplejson>=3.0',
 'streamlit-aggrid-pro>=0.2.30',
 'streamlit>=0.87.0']

setup_kwargs = {
    'name': 'streamlit-lianshan',
    'version': '0.0.4',
    'description': 'Streamlit component implementation of lianshan',
    'long_description': '# streamlit-lianshan\nstreanlit-lianshan骨架封装包，便于分析师使用\n\n<br>\n\n# Install\n```\npip install streamlit-lianshan\n\n```\n',
    'author': 'Pablo Fonseca',
    'author_email': 'yangxiaochuang2@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/llllyang123/streamlit-lianshan',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
