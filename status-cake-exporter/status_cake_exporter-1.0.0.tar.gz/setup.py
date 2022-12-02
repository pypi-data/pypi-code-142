# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['status_cake_exporter']

package_data = \
{'': ['*']}

install_requires = \
['prometheus-client==0.15.0',
 'requests>=2.28.1,<3.0.0',
 'statuscake-py>=1.0.1b1,<2.0.0',
 'typer>=0.7.0,<0.8.0',
 'types-requests>=2.28.11.4,<3.0.0.0',
 'typing-extensions>=4.4.0,<5.0.0']

entry_points = \
{'console_scripts': ['status-cake-exporter = status_cake_exporter.app:run']}

setup_kwargs = {
    'name': 'status-cake-exporter',
    'version': '1.0.0',
    'description': '',
    'long_description': '# Status Cake Exporter\n\n![status-cake-exporter](https://github.com/chelnak/status-cake-exporter/actions/workflows/ci.yml/badge.svg)\n\n> :rotating_light: Container images have moved to ghcr.io/chelnak/status-cake-exporter\n\nStatus Cake Exporter is a Prometheus exporter for [StatusCake](https://www.statuscake.com/).\n\nMetrics are exposed on port 8000 when using the provided examples/manifest.yml](examples/manifest.yml) in Kubernetes, e.g.\n\n```sh\nhttp://status-cake-exporter.default.svc:8000\n```\n\n## Requirements\n\n* Python 3.10+\n* Docker\n* Kubernetes (optional)\n* Helm 3 (optional)\n\n## Usage\n\n| Setting                              | Required | Default |\n|--------------------------------------|----------|---------|\n| API_KEY                              | Yes      | Null    |\n| TAGS                                 | No       | Null    |\n| LOG_LEVEL                            | No       | info    | \n| PORT                                 | No       | 8000    |\n\n### Docker\n\nThe following will expose the exporter at `localhost:8000`:\n\n```sh\nexport API_KEY=xxxxxxxx\ndocker run -d -p 8000:8000 --env API_KEY ghcr.io/chelnak/status-cake-exporter:latest\n```\n\n### Kubernetes\n\nTo get up and running quickly, use [examples/manifest.yml](examples/manifest.yml) as an example. You will need to create a secret named `status-cake-api-token` containing your `API_KEY` first.\n\nOtherwise, you can use the Helm Chart provided in [chart/status-cake-exporter](chart/status-cake-exporter/README.md).\n\n### Grafana\n\nTo get up and running quickly, use [examples/grafana-example.json](examples/grafana-example.json) as an example. \n\n### Terminal\n\n```sh\nUsage: status-cake-exporter [OPTIONS]\n\nOptions:\n  --api-key TEXT         API Key for the account.  [env var: API_KEY;\n                         required]\n  --tags TEXT            A comma separated list of tags used to filter tests\n                         returned from the api  [env var: TAGS]\n  --log-level TEXT       The log level of the application. Value can be one of\n                         {debug, info, warn, error}  [env var: LOG_LEVEL;\n                         default: info]\n  --port INTEGER         [env var: PORT; default: 8000]\n  --items-per-page TEXT  The number of items that the api will return on a\n                         page. This is a global option.  [env var:\n                         ITEMS_PER_PAGE; default: 25]\n  --help                 Show this message and exit\n```\n\n## Metrics\n\n| Name| Type | Description |\n|-----|------|-------------|\n| status_cake_test_info | Gauge |A basic listing of the tests under the current account. |\n| status_cake_test_uptime_percent | Gauge | Tests and their uptime percentage |\n\n## Prometheus\n\nPrometheus config needs to be updated to see the new exported. Use the following scrape config as an example:\n\n```Yaml\nscrape_configs:\n    - job_name: status-cake-exporter\n    honor_timestamps: true\n    scrape_interval: 10m\n    scrape_timeout: 1m\n    metrics_path: /\n    scheme: http\n    static_configs:\n    - targets:\n        - status-cake-exporter.default.svc:8000\n```\n\n## Grafana\n\nData collected by Prometheus can be easily surfaced in Grafana.\n\nUsing the [Statusmap panel](https://grafana.com/grafana/plugins/flant-statusmap-panel) by [flant](https://github.com/flant/grafana-statusmap) you can create a basic status visualization based on uptime percentage:\n\n![grafana](examples/grafana.png)\n\n### PromQL\n\n```PromQL\nstatus_cake_test_info * on(test_id) group_right(test_name) status_cake_test_uptime_percent\n```\n\n## Development\n\nThis repository uses [Tilt](https://tilt.dev) for rapid development on Kubernetes.\n\nTo use this, run:\n\n```sh\ncd chart/status-cake-exporter\ntilt up\n```\n\nTilt will reload your environment when it detects changes to your code.\n\nNote: You will need to provide valid credentials for StatusCake in your `Tiltfile` for this to work.\n',
    'author': 'Craig Gumbley',
    'author_email': 'craiggumbley@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
