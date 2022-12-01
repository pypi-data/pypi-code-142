# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sdevtools']

package_data = \
{'': ['*']}

install_requires = \
['importlib_metadata>=3.4.0,<4.0.0']

setup_kwargs = {
    'name': 'sha-python-devtools',
    'version': '0.1.6',
    'description': 'Python的开发工具，便于调试。',
    'long_description': "# sha-python-devtools\n\n\n[![PyPI version](https://badge.fury.io/py/sha-python-devtools.svg)](https://badge.fury.io/py/sha-python-devtools)\n![versions](https://img.shields.io/pypi/pyversions/sha-python-devtools.svg)\n[![GitHub license](https://img.shields.io/github/license/mgancita/sha-python-devtools.svg)](https://github.com/mgancita/sha-python-devtools/blob/main/LICENSE)\n\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\nPython的开发工具，便于调试。\n\n## 来自\n来自python-devtools 工具，准备用来进行自定义操作。\n\n## 版本\n\nv0.1.6 修改`timer.py`  解决 `name 'Timer' is not defined` 问题。\n\n- 开源许可: MIT\n- 文档: https://llango.github.io/sha-python-devtools.\n\n\n## 特征\n\n* TODO\n\n## 制作\n\n\n该包使用 [Cookiecutter](https://github.com/audreyr/cookiecutter) 和 [`llango/cookiecutter-mkdoc-shapackage`](https://github.com/llango/cookiecutter-mkdoc-shapackage/) 项目模版创建。\n",
    'author': 'Rontomai',
    'author_email': 'rontomai@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/llango/sha-python-devtools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
