# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['compose_companion']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0',
 'pyyaml>=6.0,<7.0',
 'rich>=12.6.0,<13.0.0',
 'typer>=0.7.0,<0.8.0',
 'yaml-env-var-parser>=1.1.1,<2.0.0']

entry_points = \
{'console_scripts': ['compose = compose_companion.cli:app']}

setup_kwargs = {
    'name': 'compose-companion',
    'version': '0.1.4',
    'description': 'A companion for Docker Compose',
    'long_description': "# Compose Companion\n\nThis is a little CLI tool created for my home server.\n\nIt aims to make it easy to configure and document scripts that should run before and/or after the server containers on docker compose go up or down.\n\n## Scrips File\n\nThe app will read the scripts from a yaml file in the following format:\n\n```yaml\n# compose-companion.yaml\n\nx-before-up:\n  sonarr:\n    - echo this will run before sonarr startup\n    - echo this too will run before sonarr startup, after the previous one\n  radarr:\n    - echo this will run before radarr startup\n    - echo this too will run before radarr startup, after the previous one\n\nx-after-up:\n  sonarr:\n    - echo this will run after sonarr startup\n    - echo this too will run after sonarr startup, after the previous one\n  radarr:\n    - echo this will run after radarr startup\n    - echo this too will run after radarr startup, after the previous one\n\nx-before-down:\n  sonarr:\n    - echo this will run before sonarr shutdown\n    - echo this too will run before sonarr shutdown, after the previous one\n  radarr:\n    - echo this will run before radarr shutdown\n    - echo this too will run before radarr shutdown, after the previous one\n\nx-after-down:\n  sonarr:\n    - echo this will run after sonarr shutdown\n    - echo this too will run after sonarr shutdown, after the previous one\n  radarr:\n    - echo this will run after radarr shutdown\n    - echo this too will run after radarr shutdown, after the previous one\n```\n\nThe container keys should match the ones from `docker-compose.yaml` file.  \nThe app will look for a file named `compose-companion.yaml` on the folder it's first run, if that's not there it'll ask you to inform the file path manually.  \nAs the top-level keys start with `x-`, you can use the `docker-compose.yaml` file itself, if you wish, and these settings will be properly ignored by docker compose.\n\n## Commands\n\n```plain\n╭─ Commands ──────────────────────────────────────────────────────────────────────────────╮\n│ config        View or change configurations.                                            │\n│                                                                                         │\n│ down          Shuts down target containers. If no target is defined, shuts down all     │\n│               containers. Equivalent to `docker compose rm -sf`.                        │\n│                                                                                         │\n│ exec          Runs command on the container. Equivalent to `docker compose exec`.       │\n│                                                                                         │\n│ logs          Prints logs for target containers. If no target is defined, prints for    │\n│               all running ones. Equivalent to `docker compose logs -f`                  │\n│                                                                                         │\n│ pause         Pauses targeted containers. If no target is defined, pauses all           │\n│               containers. Equivalent to `docker compose pause`.                         │\n│                                                                                         │\n│ ps            Lists containers. If no target is defined, lists all containers.          │\n│               Equivalent to `docker compose ps`.                                        │\n│                                                                                         │\n│ start         Starts targeted containers. If no target is defined, starts all           │\n│               containers. Equivalent to `docker compose start`.                         │\n│                                                                                         │\n│ stop          Stops targeted containers. If no target is defined, stops all containers. │\n│               Equivalent to `docker compose stop`.                                      │\n│                                                                                         │\n│ up            Starts up targeted containers. If no target is defined, starts all        │\n│               containers. Calls to `docker compose up -d --remove-orphans`.             │\n╰─────────────────────────────────────────────────────────────────────────────────────────╯\n```\n\nFor more details on each command, run `compose [command] --help`\n",
    'author': 'Natália Fonseca',
    'author_email': 'natalia@nataliafonseca.dev',
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
