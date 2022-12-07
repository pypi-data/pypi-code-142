# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starlite_starception']

package_data = \
{'': ['*'], 'starlite_starception': ['templates/*']}

install_requires = \
['Jinja2>=3,<4', 'MarkupSafe>=2,<3', 'starlite', 'typing_extensions>=4.4,<5.0']

setup_kwargs = {
    'name': 'starlite-starception',
    'version': '1.0.1.1',
    'description': 'Beautiful debugging page for starlite apps.',
    'long_description': '##############\n\n# NOTE: this is a fork of https://github.com/alex-oleshkevich/starception\n\nAll rights to him and the contributors for that repo.\n\nThis fork exists to implement starception for starlite: https://github.com/starlite-api/starlite.\n\nStarlite left starlette since version [1.39.0] for there own implementations. \n\nTherefore the orginal repo doens\'t work\nanymore\n\nSeeing starception was originally built for starlette backed frameworks.\nSo a fork was needed to make this work with\nstarlite\n\nNote2 : I will keep the fork in sync with the main repo except for the starlette stuff.\n\n##############\n\n# Starception-starlite\n\nBeautiful exception page for Starlette and FastAPI apps.\n\n![PyPI](https://img.shields.io/pypi/v/starception)\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alex-oleshkevich/starception/Lint%20and%20test)\n![GitHub](https://img.shields.io/github/license/alex-oleshkevich/starception)\n![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/starception)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/starception)\n![GitHub Release Date](https://img.shields.io/github/release-date/alex-oleshkevich/starception)\n\n## Installation\n\nInstall `starlite-starception` using PIP or poetry:\n\n```bash\npip install starlite_starception\n# or\npoetry add starlite_starception\n```\n\n### With syntax highlight support\n\nIf you want to colorize code snippets, install `pygments` library.\n\n```bash\npip install starlite_starception[pygments]\n# or\npoetry add starlite_starception -E pygments\n```\n\n## Screenshot\n\n![image](screenshot.png)\n\n<details>\n<summary>Dark theme</summary>\n<div>\n    <img src="./dark.png">\n</div>\n</details>\n\n## Features\n\n* secrets masking\n* solution hints\n* code snippets\n* display request info: query, body, headers, cookies\n* session contents\n* request and app state\n* platform information\n* environment variables\n* syntax highlight\n* open paths in editor (vscode only)\n* exception chains\n* dark theme\n\nThe middleware will automatically mask any value which key contains `key`, `secret`, `token`, `password`.\n\n## Quick start\n\nSee example application in [examples/](examples/) directory of this repository.\n\n## Usage\n\nStarception will work only in debug mode so don\'t forget to set `debug=True` for local development.\n\n### Monkey patching Starlette\n\nTo replace built-in debug exception handler call `install_error_handler` before you create Starlette instance.\n> Currently, this is a recommended approach.\n\n```python\nfrom starlite_starception import install_error_handler\nfrom starlite import Starlite, get\n\n\n@get("/")\ndef view() -> None:\n    raise TypeError(\'Oops\')\n\n\ninstall_error_handler()\napp = Starlite(route_handlers=[view])\n```\n\n### Using middleware\n\nTo render a beautiful exception page you need to install a `StarceptionMiddleware` middleware to your application.\n\n\n> Note, to catch as many exceptions as possible the middleware has to be the first one in the stack.\n\n```python\nimport typing\n\nfrom starlite import Starlite\n\nfrom starlite_starception import StarceptionMiddleware\n\n\nasync def index_view() -> None:\n    raise Exception(\'Oops, something really went wrong...\')\n\n\napp = Starlite(\n    debug=True,\n    route_handlers=[index_view],\n    middleware=[\n        StarceptionMiddleware,\n        # other middleware go here\n    ]\n)\n```\n\n## Solution hints\n\nIf exception class has `solution` attribute then its content will be used as a solution hint.\n\n```python\nclass WithHintError(Exception):\n    solution = (\n        \'The connection to the database cannot be established. \'\n        \'Either the database server is down or connection credentials are invalid.\'\n    )\n```\n\n![image](hints.png)\n\n## Opening files in editor\n\nSet your current editor to open paths in your editor/IDE.\n\n```python\nfrom starlite_starception import set_editor\n\nset_editor(\'vscode\')\n```\n\n![image](link.png)\n\n\n> Note, currently only VSCode supported. If you know how to integrate other editors - please PR\n\n### Registering link templates\n\nIf your editor is not supported, you can add it by calling `add_link_template` and then selecting it with `set_editor`.\n\n```python\nfrom starlite_starception import set_editor, add_link_template\n\nadd_link_template(\'vscode\', \'vscode://file/{path}:{lineno}\')\nset_editor(\'vscode\')\n```\n\n## Credentials\n\n* Look and feel inspired by [Phoenix Framework](https://www.phoenixframework.org/).\n* Icons by [Tabler Icons](https://tabler-icons.io/).\n',
    'author': 'Alex Oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nielsvanhooy/starlite-starception',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
