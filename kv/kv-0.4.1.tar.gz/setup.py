# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['kv']
entry_points = \
{'console_scripts': ['kv-cli = kv:main']}

setup_kwargs = {
    'name': 'kv',
    'version': '0.4.1',
    'description': 'KV provides a dictionary-like interface on top of SQLite.',
    'long_description': "KV - simple key/value store\n===========================\n\n.. image:: https://github.com/mgax/kv/actions/workflows/ci.yml/badge.svg?branch=master\n\nKV provides a dictionary-like interface on top of SQLite. Keys can be\nunicode strings, numbers or None. Values are stored as JSON.\n\n::\n\n    >>> from kv import KV\n    >>> db = KV('/tmp/demo.kv')\n    >>> db['hello'] = 'world'\n    >>> db[42] = ['answer', 2, {'ultimate': 'question'}]\n    >>> dict(db)\n    {42: [u'answer', 2, {u'ultimate': u'question'}], u'hello': u'world'}\n\n\nThere is a locking facility that uses SQLite's transaction API::\n\n    >>> with kv.lock():\n    ...   l = db[42]\n    ...   l += ['or is it?']\n    ...   db[42] = l\n\n\nAnd that's about it. The code_ is really simple.\n\n.. _code: https://github.com/mgax/kv\n",
    'author': 'Alex Morega',
    'author_email': 'alex@grep.ro',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
