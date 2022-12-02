# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bornrule', 'bornrule.sql', 'bornrule.torch']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.5', 'pandas>=1.1.5', 'scikit-learn>=0.24.2', 'scipy>=1.5.4']

setup_kwargs = {
    'name': 'bornrule',
    'version': '0.1.3',
    'description': "Classification with Born's rule",
    'long_description': '<img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/08/Logo_for_Conference_on_Neural_Information_Processing_Systems.svg/1200px-Logo_for_Conference_on_Neural_Information_Processing_Systems.svg.png" align="right" height="128"/>This package implements the classifier proposed in:\n\n> Emanuele Guidotti and Alfio Ferrara. Text Classification with Born’s Rule. *Advances in Neural Information Processing Systems*, 2022.\n\n<div align="center">\n  [<a href="https://github.com/eguidotti/bornrule">GitHub</a>] - \n  [<a href="https://eguidotti.github.io/bornrule/">Docs</a>] - \n  [<a href="https://openreview.net/pdf?id=sNcn-E3uPHA">Paper</a>] - \n  [<a href="https://nips.cc/media/neurips-2022/Slides/54723.pdf">Slides</a>] - \n  [<a href="https://nips.cc/media/PosterPDFs/NeurIPS%202022/8d7628dd7a710c8638dbd22d4421ee46.png">Poster</a>]\n</div>\n\n',
    'author': 'Emanuele Guidotti',
    'author_email': 'emanuele.guidotti@unine.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eguidotti/bornrule',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
