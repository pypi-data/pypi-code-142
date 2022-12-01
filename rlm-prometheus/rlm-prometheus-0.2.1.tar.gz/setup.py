# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rlm_prometheus']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'loguru>=0.6.0,<0.7.0',
 'lxml>=4.9.1,<5.0.0',
 'pandas>=1.5.1,<2.0.0',
 'prometheus-client>=0.15.0,<0.16.0',
 'python-box>=6.1.0,<7.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['rlm_exporter = rlm_prometheus.cli:run_rlm_exporter']}

setup_kwargs = {
    'name': 'rlm-prometheus',
    'version': '0.2.1',
    'description': 'Prometheus metrics collector and exporter for RLM (Reprise License Manager)',
    'long_description': "# RLM-Prometheus\n\n[Prometheus][1] exporter providing metrics from a Reprise License Manager (RLM)\ninstance.\n\n## Installation\n\nExample installation on Debian / Ubuntu:\n\n```bash\n# required for creating Python virtualenvs:\napt install python3-venv\n\n# create a virtualenv in /opt:\npython3 -m venv /opt/rlm-exporter\n\n# update 'pip' and install the 'rlm-exporter' package:\n/opt/rlm-exporter/bin/pip install --upgrade pip\n/opt/rlm-exporter/bin/pip install rlm-exporter\n```\n\n## Running in foreground mode\n\nThis is mostly relevant for testing configuration settings and checking if the\nexporter works as expected - to do this either activate the previously created\nPython environment or call the `rlm_exporter` script using the full path to that\nenvironment.\n\nFor convenience it is reasonable to use a configuration file in such a situation\ninstead of setting all the environment variables manually. Simply copy the\n[config-example.yaml][3] file to e.g. `config.yaml` and adjust the settings\nthere. Then run the exporter like this:\n\n```bash\nrlm_exporter -vvv --config config.yaml\n```\n\nThe exporter running in foreground can be terminated as usual via `Ctrl+C`.\n\n## Running as a service\n\n```bash\nadduser --system rlmexporter\ncp -v /opt/rlm-exporter/lib/python*/site-packages/resources/systemd/rlm-exporter.service  /etc/systemd/system/\nsystemctl daemon-reload\nsystemctl edit rlm-exporter.service\n```\n\nThe last command will open an editor with the override configuration of the\nservice's unit file. Add a section like this **at the top** of the override\nfile, with the bare minimum of setting `RLM_ISV` and most likely also `RLM_URI`.\nFor other options available check for the commented-out lines further down in\nthe unit file setting environment variables starting with `RLM_`.\n\n```text\n[Service]\n### specific configuration for the RLM exporter service:\nEnvironment=RLM_ISV=example_isv\nEnvironment=RLM_URI=http://license-server.example.xy:5054\n```\n\nFinally enable the service and start it right away. The second line will show\nthe log messages on the console until `Ctrl+C` is pressed. This way you should\nbe able to tell if the service has started up properly and is providing metrics\non the configured port:\n\n```bash\nsystemctl enable --now rlm-exporter.service\njournalctl --follow --unit rlm-exporter\n```\n\n## Firewall settings for RLM on Windows\n\nFor the metrics collection it is obviously necessary the exporter can gather data from\nyour RLM instance. The standard approach is to send requests to RLM's built-in web\nserver. By default access to it is blocked and those restrictions should not be lifted\nmore than necessary.\n\nThere is an example snippet in [Open-RlmFirewallPort.ps1][2] that demonstrates how to\nadjust the Windows firewall so the collector's host IP address is allowed to connect\nto RLM.\n\n[1]: https://prometheus.io/\n[2]: resources/powershell/Open-RlmFirewallPort.ps1\n[3]: resources/config-example.yaml\n",
    'author': 'Niko Ehrenfeuchter',
    'author_email': 'nikolaus.ehrenfeuchter@unibas.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/rlm-prometheus/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
