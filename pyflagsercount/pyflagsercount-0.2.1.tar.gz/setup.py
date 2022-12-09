# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyflagsercount']

package_data = \
{'': ['*'], 'pyflagsercount': ['include/*', 'src/*']}

install_requires = \
['numpy>=1.17.0']

setup_kwargs = {
    'name': 'pyflagsercount',
    'version': '0.2.1',
    'description': 'A program for counting directed cliques in directed graphs',
    'long_description': '# flagser-count\nA program for counting directed cliques in directed graphs, adapted from https://github.com/luetge/flagser\n\nTo install, first download repository with:\n```sh\ngit clone --recursive https://github.com/JasonPSmith/flagser-count.git\n```\nNext, compile flagser count with\n```\nmake\n```\n\nTo verify that flagser-count has installed correctly run:\n\n```sh\n(cd test && python run_test.py && cd ..)\n```\n\nTo install pyflagsercount run:\n```sh\npip install .\n```\nRequirements: For pyflagsercount the packages numpy and pybind11 are required, and cmake version ≥ 2.8.12.\n',
    'author': 'jasonpsmith',
    'author_email': 'jasonsmith.bath@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
