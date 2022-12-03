# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyopera', 'pyopera.opera', 'pyopera.opera.helpers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyopera',
    'version': '0.1.0',
    'description': 'The NIH OPERA suite of models with Python specific functionality',
    'long_description': '# pyOPERA\nFull python implementation of the NIH OPERA suite of models  \ndocker run -it -v %cd%:/app --rm pyopera_pyopera /bin/bash  \ndocker compose -f docker-compose.yml build  \ndocker run --rm pyopera_pyopera ~/.local/share/pypoetry/venv/bin/poetry run coverage run -m pytest tests  \ndocker build -t cabreratoxy/pyopera:0.0.1 .  \n\n```\npoetry run python -m pip install -r requirements.txt  \npoetry run black .  \npoetry run isort .  \npoetry run pylint $(find . -name "*.py" | xargs)  \npoetry run pytest tests    \npoetry run coverage run --source pyopera -m pytest  \npoetry run coverage report --skip-empty --fail-under=85  \n\ndocker run --rm pyopera_pyopera /bin/bash -c \'poetry run coverage run -m pytest tests\'   \n```\n\n~~TODO: Create a python package around the Matlab package (the base files) using Poetry~~  \nTODO: Create CI/CD for package in TestPypi and the prod Pypi (CircleCI maybe?)  \n~~TODO: Auto semantic versioning with poetry too~~  \nTIDO: Documentation using Sphinx (make sure original repo/builders are credited)  \nTODO: Start adding the wrapper code and files - in progress    \nTODO: Benchmarking with airspeed velocity  \n~~TODO: Formatting/Linting/Coverage~~  \n~~TODO: Choose between Pytest an Unittest~~  \nTODO: Don\'t repeat the library name in the Dockerfile  \n~~TODO: Automate black, isort, pylint, coverage, pytest on build or push. - just have to finish coverage~~\nTODO: Struggling to run commands inside Docker from the host, will run commands from inside container for now  \n~~TODO: Auto docstring generating? -- used autodocstring extension for vscode~~  \n~~TODO: How to autobuild the base image the CI/CD will work with - could not be done~~  \n',
    'author': 'Manuel Cabrera',
    'author_email': 'cabrera.manuel555@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
