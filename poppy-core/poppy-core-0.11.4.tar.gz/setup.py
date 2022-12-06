# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poppy',
 'poppy.core',
 'poppy.core.conf',
 'poppy.core.db',
 'poppy.core.db.models',
 'poppy.core.generic',
 'poppy.core.management',
 'poppy.core.management.templates.pipeline_template',
 'poppy.core.target',
 'poppy.core.task',
 'poppy.core.tools',
 'poppy.core.tools.appdirs',
 'poppy.core.tools.cdf',
 'poppy.core.tools.poppy_logging',
 'poppy.core.tools.test',
 'poppy.core.tools.xmltodict']

package_data = \
{'': ['*'],
 'poppy.core.management': ['templates/plugin_template/*',
                           'templates/plugin_template/plugin_namespace/*',
                           'templates/plugin_template/plugin_namespace/plugin_name/*',
                           'templates/plugin_template/plugin_namespace/plugin_name/models/*',
                           'templates/plugin_template/plugin_namespace/plugin_name/models/versions/*']}

install_requires = \
['SQLAlchemy>=1.3,<2.0',
 'alembic>=1.4,<2.0',
 'declic>=1.0,<2.0',
 'jsonschema>=4.0,<5.0',
 'psycopg2-binary>=2.8.4,<3.0.0']

entry_points = \
{'console_scripts': ['poppy = poppy.core.management.commands:poppy_cli']}

setup_kwargs = {
    'name': 'poppy-core',
    'version': '0.11.4',
    'description': 'POPPy: Plugin-Oriented Pipeline for Python',
    'long_description': 'poppy-core\n===========\n\n[![pipeline status](https://gitlab.obspm.fr/POPPY/POPPyCore/badges/develop/pipeline.svg)](https://gitlab.obspm.fr/POPPY/POPPyCore/pipelines)\n\nThis directory contains the source code of the POPPY framework core.\n\n## Quickstart\n\nTo install package using [pip](https://pypi.org/project/pip-tools/):\n\n```\npip install poppy-core --extra-index-url https://__token__:<your_personal_token>@gitlab.obspm.fr/api/v4/projects/2052/packages/pypi/simple --trusted-host gitlab.obspm.fr\n```\n\nTo install package from source files:\n\n```\ngit clone https://gitlab.obspm.fr/POPPY/POPPyCore.git poppy-core\n```\n\nThen install using [pip](https://pypi.org/project/pip-tools/):\n\n```\ncd poppy-core\npip install .\n```\n\nor using [poetry](https://python-poetry.org/):\n\n```\ncd poppy-core\npip install poetry\npoetry install\n```\n\n## User guide\n\nSee "POPPY User Manual" for more details.\n\n## License\n\nPOPPY is under CeCILL license.\n\n## Acknowledgement\n\nPOPPY is project developed by the RPW Operations Centre (ROC) team based at LESIA (Meudon, France).\nThe ROC is funded by the Centre National d\'Etudes Spatiale (CNES) in the framework of the European Space Agency (ESA) Solar Orbiter mission.\n\n## Authors\n\nxavier.bonnin@obspm.fr (project manager)\n\n\nHas also contributed in the past: Sonny Lion, Gregoire Duvauchelle, Manuel Duarte\n',
    'author': 'Xavier Bonnin',
    'author_email': 'xavier.bonnin@obspm.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.obspm.fr/POPPy/POPPyCore',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
