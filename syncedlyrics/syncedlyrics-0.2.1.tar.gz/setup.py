# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['syncedlyrics', 'syncedlyrics.providers']

package_data = \
{'': ['*']}

install_requires = \
['rapidfuzz>=2.13.2,<3.0.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['syncedlyrics = syncedlyrics.cli:cli_handler']}

setup_kwargs = {
    'name': 'syncedlyrics',
    'version': '0.2.1',
    'description': 'Get an LRC format (synchronized) lyrics for your music',
    'long_description': '# syncedlyrics\n Get an LRC format (synchronized) lyrics for your music.\n\n## Installation\n```\npip install syncedlyrics\n```\n## Usage\n### CLI\n```\nsyncedlyrics "SEARCH_TERM"\n```\n#### Available Options\n| Flag | Description |\n| --- | --- |\n| `-o` | Path to save `.lrc` lyrics, default="{search_term}.lrc" |\n| `-v` | Use this flag to show the logs |\n| `--allow-plain` | Return a plain text (not synced) lyrics if not LRC was found |\n\n### Python\n```py\nimport syncedlyrics\nlrc = syncedlyrics.search("[TRACK_NAME] [ARTIST_NAME]")\n```\nOr with options:\n```py\nsyncedlyrics.search("...", allow_plain_format=True, save_path="{search_term}_1234.lrc", providers=["Deezer"])\n```\n\n## Providers\n- NetEase (music.163.com)\n- Deezer\n\nFeel free to suggest more providers please.\n\n## License\n[MIT](https://github.com/rtcq/syncedlyrics/blob/master/LICENSE)\n\n## Notes\nI also found a [repo](https://github.com/fashni/MxLRC) for Musixmatch API, but it has annoying API rate limits at the moment\n',
    'author': 'Momo',
    'author_email': 'lo3me@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
