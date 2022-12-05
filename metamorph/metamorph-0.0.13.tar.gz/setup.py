# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metamorph']

package_data = \
{'': ['*']}

install_requires = \
['colorama', 'deep_translator', 'pyyaml', 'termcolor']

entry_points = \
{'console_scripts': ['metamorph = metamorph.main:__main__']}

setup_kwargs = {
    'name': 'metamorph',
    'version': '0.0.13',
    'description': 'Metamorph text into other reworded text.',
    'long_description': '# metamorph\n\n![IMG](/img/img.png)\n\nFirst line is the input followed by colorized suggestions.\n\nDoc: `metamorph --help`\n\n[![PyPI version][pypi image]][pypi link]  ![downloads](https://img.shields.io/pypi/dm/metamorph.svg) \n\n| [Stable][doc release]        | [Unstable][doc test]           |\n| ------------- |:-------------:|\n| [![workflow][a s image]][a s link]      | [![test][a t image]][a t link]     |\n| [![Coverage Status][c s i]][c s l] | [![Coverage Status][c t i]][c t l] |\n| [![Codacy Badge][cc s c i]][cc s c l]      |[![Codacy Badge][cc c i]][cc c l] | \n| [![Codacy Badge][cc s q i]][cc s q l]     |[![Codacy Badge][cc q i]][cc q l] | \n| [![Documentation][rtd s i]][rtd s l] | [![Documentation][rtd t i]][rtd t l]  | \n\n## Documentation\n\n-   <https://metamorph-apn.readthedocs.io/en/stable/>\n-   <https://apn-pucky.github.io/metamorph/index.html>\n\n## Versions\n\n### Stable\n\n```sh\npip install metamorph [--user] [--upgrade]\n```\n\n### Dev\n\n```sh\npip install --index-url https://test.pypi.org/simple/ metamorph [--user] [--upgrade]\n```\n\n## Configuration\n\nFor a list of parameters run `metamorph -h`.\n\nThe root node `flow` can have multiple different starting languages (given `start` is None).\n```yaml\ntranslator: "GoogleTranslator"\nstart: "de"\ngoal: "de"\n\nflow:\n  de:\n    fr:\n      es:\n        fr:\n    de:\n      es:\n      fr:\n        sv:\n  fr:\n    en:\n  en:\n  fi:\n    de:\n      fr:\n        es:\n          fr:\n      de:\n        es:\n        fr:\n          sv:\n  sv:\n```\n\nThis exemplary `configs/config.yaml` will produce following results (note `-sd` for diagrams and `-c` for config, while most command line parameters take precedence over config (`-gs` here)).\nA list of translators can be found here <https://github.com/nidhaloff/deep-translator>.\n\n```sh\nmetamorph -i -sd -gs en -c config.yaml\n```\n\n![DIAG](/img/diag.png)\n\n(`GoogleTranslate` gets abbreviated to only capital letters `GT`)\n\n[doc release]: https://apn-pucky.github.io/metamorph/index.html\n[doc test]: https://apn-pucky.github.io/metamorph/test/index.html\n\n[pypi image]: https://badge.fury.io/py/metamorph.svg\n[pypi link]: https://pypi.org/project/metamorph/\n\n[a s image]: https://github.com/APN-Pucky/metamorph/actions/workflows/stable.yml/badge.svg\n[a s link]: https://github.com/APN-Pucky/metamorph/actions/workflows/stable.yml\n[a t link]: https://github.com/APN-Pucky/metamorph/actions/workflows/unstable.yml\n[a t image]: https://github.com/APN-Pucky/metamorph/actions/workflows/unstable.yml/badge.svg\n\n[cc s q i]: https://app.codacy.com/project/badge/Grade/1acfcad112734b1ca875518cf1eeda34?branch=stable\n[cc s q l]: https://www.codacy.com/gh/APN-Pucky/metamorph/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/metamorph&amp;utm_campaign=Badge_Grade?branch=stable\n[cc s c i]: https://app.codacy.com/project/badge/Coverage/1acfcad112734b1ca875518cf1eeda34?branch=stable\n[cc s c l]: https://www.codacy.com/gh/APN-Pucky/metamorph/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/HEPi&utm_campaign=Badge_Coverage?branch=stable\n\n[cc q i]: https://app.codacy.com/project/badge/Grade/1acfcad112734b1ca875518cf1eeda34\n[cc q l]: https://www.codacy.com/gh/APN-Pucky/metamorph/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/metamorph&amp;utm_campaign=Badge_Grade\n[cc c i]: https://app.codacy.com/project/badge/Coverage/1acfcad112734b1ca875518cf1eeda34\n[cc c l]: https://www.codacy.com/gh/APN-Pucky/metamorph/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/HEPi&utm_campaign=Badge_Coverage\n\n[c s i]: https://coveralls.io/repos/github/APN-Pucky/metamorph/badge.svg?branch=stable\n[c s l]: https://coveralls.io/github/APN-Pucky/metamorph?branch=stable\n[c t l]: https://coveralls.io/github/APN-Pucky/metamorph?branch=master\n[c t i]: https://coveralls.io/repos/github/APN-Pucky/metamorph/badge.svg?branch=master\n\n[rtd s i]: https://readthedocs.org/projects/metamorph/badge/?version=stable\n[rtd s l]: https://metamorph-apn.readthedocs.io/en/stable/?badge=stable\n[rtd t i]: https://readthedocs.org/projects/metamorph/badge/?version=latest\n[rtd t l]: https://metamorph-apn.readthedocs.io/en/latest/?badge=latest\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
