# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emllib',
 'emllib.dataclass',
 'emllib.dataclass.eml220',
 'emllib.gends',
 'emllib.pyxb']

package_data = \
{'': ['*'], 'emllib': ['schemas/eml/eml-2.1.1/*', 'schemas/eml/eml-2.2.0/*']}

install_requires = \
['mdutils>=1.4.0,<2.0.0', 'xsdata[lxml]==22.9']

setup_kwargs = {
    'name': 'pyemllib',
    'version': '0.2.0',
    'description': 'Python lib to deal with EML (Ecological Metadata Language)',
    'long_description': '# pyemllib\n\n[![Release](https://img.shields.io/pypi/v/pyemllib.svg)](https://pypi.org/pypi/pyemllib/)\n[![Build status](https://img.shields.io/github/workflow/status/jusana/pyemllib/merge-to-main)](https://img.shields.io/github/workflow/status/jusana/pyemllib/merge-to-main)\n[![codecov](https://codecov.io/gh/jusana/pyemllib/branch/main/graph/badge.svg)](https://codecov.io/gh/jusana/pyemllib)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/jusana/pyemllib)](https://img.shields.io/github/commit-activity/m/jusana/pyemllib)\n[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://jusana.github.io/pyemllib/)\n[![Code style with black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports with isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)\n[![License](https://img.shields.io/github/license/jusana/pyemllib)](https://img.shields.io/github/license/jusana/pyemllib)\n\nThis package is a python lib to help dealing with EML - Ecological Metadata Language.\n\nIt\'s built uppon [dataclasses](https://docs.python.org/3.9/library/dataclasses.html) generated with [xsdata](https://github.com/tefra/xsdata) from [EML xsd](https://eml.ecoinformatics.org/schema/) hence heavily relies on xsdata capabilities\n\n*For history reasons, i also provide the former pyxb and generateDS (built with py38) that i used to use on my projects but that i now find\nmore cumbersome to use than the dataclass implementation. They might be useful anyway !!*\n\n\nNB: This lib is currently developped under a local gitlab forge and will be release on github on important releases\n- *Github repository*: <https://github.com/jusana/pyemllib/>\n- *Documentation* <https://jusana.github.io/pyemllib/>\n\n\n## Main features\n\n- Deserializes EML files to python objects\n- Serializes pure python objects to EML as XML string / files\n- Checks validity of EML generated against xsd \n- Generates a markdown/html DataPaper from suitable EML files\n- \n\n\n## Very simple usage\n\n\n```python\nfrom emllib import EMLizer\n\n# instantiate EML object document\nmy_eml = EMLizer(package_id="ID", title="Mon titre", lang="fr", creator="Mon Createur", abstract="Mon abstract")\n\n# print EML xml formatted string\nprint(my_eml.to_string())\n\n# dump EML xml formatted to file\nmy_eml.to_file(\'path/to/file/eml.xml\')\n\n# Inspect validity\nif my_eml.validate().bool:\n    print("This EML file seems valid")\nelse:\n    print("This EML file does not seem valid!")\n    my_eml.validate().reason\n\n```\n\n\n## Recommended usage\n\nThe EMLizer helper class is just a wrapper to help quickly basic EML files.\nNevertheless in more complex or sophisticated situations, i recommend to use the dataclass API directly under `emllib.dataclass.eml220`\n\n\n\n# Changelog\n\n## 0.2.0\n\n### Added\n\n### Changed\n\n* utils.validate() returns collections.namedtuple (bool, reason) instead of just bool\n\n### Removed\n\n\n---\n\nRepository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).',
    'author': 'Julien Sananikone',
    'author_email': 'julien.sananikone@mnhn.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jusana/pyemllib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<=3.11',
}


setup(**setup_kwargs)
