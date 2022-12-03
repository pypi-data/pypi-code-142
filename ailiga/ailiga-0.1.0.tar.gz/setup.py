# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ailiga',
 'ailiga.APNPucky.DQNFighter',
 'ailiga.APNPucky.DRDQNFighter',
 'ailiga.APNPucky.PPOFighter',
 'ailiga.APNPucky.RandomFigher']

package_data = \
{'': ['*']}

install_requires = \
['PettingZoo<1.22.0',
 'SuperSuit',
 'cfg_load',
 'pyglet==1.5.27',
 'rlcard',
 'tianshou==0.4.10',
 'torch==1.13.0',
 'tqdm']

setup_kwargs = {
    'name': 'ailiga',
    'version': '0.1.0',
    'description': '',
    'long_description': '# AILiga\n\n\n## Installation\n\n```sh\npoerty install\npoetry shell\n```\n\n\n\n\n## Testing and Training\n\nCurrently, training/testing fighters works through the fighter tests.\n```sh\npython tests/test_dqn_fighter.py\n```\n\n## Tensorboard\n\n```sh\ntensorboard --logdir log/ --load_fast=false\n```\n\n\n## Limitations\n\nCurrently, the implementation through `tianshou.BasePolicy` seems to only support DQNPolicy and also not `Discrete()` observation spaces.\n\n## References\n\n### Frameworks\n\n* https://github.com/Farama-Foundation/PettingZoo\n* https://github.com/vwxyzjn/cleanrl\n* https://github.com/Farama-Foundation/Gymnasium\n* https://github.com/deepmind/open_spiel\n* https://github.com/datamllab/rlcard\n* https://tianshou.readthedocs.io/en/master/\n\n### Books\n\n* http://incompleteideas.net/book/the-book-2nd.html\n\n\n## Development\n\nWe use black through\n\n### package/python structure:\n\n* https://mathspp.com/blog/how-to-create-a-python-package-in-2022\n* https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
