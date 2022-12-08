# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ldimbenchmark',
 'ldimbenchmark.datasets',
 'ldimbenchmark.generator',
 'ldimbenchmark.methods']

package_data = \
{'': ['*']}

install_requires = \
['big-o>=0.10.2,<0.11.0',
 'docker>=6.0.1,<7.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'tabulate>=0.9.0,<0.10.0',
 'tqdm>=4.64.1,<5.0.0',
 'wntr>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'ldimbenchmark',
    'version': '0.1.0',
    'description': '',
    'long_description': '# LDIMBenchmark\n\nLeakage Detection and Isolation Methods Benchmark\n\n## Roadmap\n\n- v1: Just Leakage Detection\n- v2: Provides Benchmark of Isolation Methods\n\nhttps://mathspp.com/blog/how-to-create-a-python-package-in-2022\n\n## Development\n\nhttps://python-poetry.org/docs/basic-usage/\n\n```bash\n# Use Environment\npoetry config virtualenvs.in-project true\npoetry shell\npoetry install --without ci # --with ci\n\n\n# Test\npoetry build\ncp -r dist tests/dist\ncd tests\ndocker build . -t testmethod\npytest -s -o log_cli=true\n\n# Test-Publish\npoetry config repositories.testpypi https://test.pypi.org/legacy/\npoetry config http-basic.testpypi __token__ pypi-your-api-token-here\npoetry build\npoetry publish -r testpypi\n\n# Real Publish\npoetry config pypi-token.pypi pypi-your-token-here\n```\n\n### Documentation\n\nhttps://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/\n\n```\nmkdocs serve\n```\n',
    'author': 'DanielHabenicht',
    'author_email': 'daniel-habenicht@outlook.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
