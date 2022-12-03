# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloud_cloner']

package_data = \
{'': ['*']}

install_requires = \
['dacite>=1.6.0,<2.0.0',
 'python-rclone>=0.0.2,<0.0.3',
 'pyyaml>=6.0,<7.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['cloud-cloner = cloud_cloner.run:app']}

setup_kwargs = {
    'name': 'cloud-cloner',
    'version': '0.1.2',
    'description': 'Tool for cloning data from cloud storage services in a configurable way',
    'long_description': 'A tool for cloning data from cloud storage providers in a configurable way.\n\nExample config file:\n```yaml\nbase_path: /base_path\nclones:\n  - name: clone_one_folder\n    paths:\n      - src: path/to/remote/folder\n        dest: path/to/local/folder\n    default: true\n  - name: clone_files\n    paths:\n      - src: files/file.txt\n        dest: remote_files/file_renamed.txt\n      - src: files/file2.txt\n        dest: remote_files/\n```\n\nThe config file is expected to be in the current working directory and named `cloud_cloner.yaml`. This location can be set with `--config-path`.\n\nA valid rclone config is expected at `~/.rclone`. This location can be set with `--rclone-config-path`. \n\nThen clone with `python -m cloud_cloner clone` or `python -m cloud_cloner clone clone_one_folder`.\n\nSee `python -m cloud_cloner --help` for more options.\n',
    'author': 'Omegastick',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
