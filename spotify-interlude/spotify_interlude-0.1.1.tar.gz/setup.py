# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spotify_interlude']

package_data = \
{'': ['*']}

install_requires = \
['pycaw>=20220416,<20220417',
 'pydantic>=1.9.1,<2.0.0',
 'pywin32>=305,<306',
 'spotipy>=2.20.0,<3.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['interlude = spotify_interlude.cli:app']}

setup_kwargs = {
    'name': 'spotify-interlude',
    'version': '0.1.1',
    'description': 'Pause Spotify playback when other apps start making noise',
    'long_description': "_Pause Spotify playback when other apps start making noise on Windows._\n_Automatically resume playback when the other sound finishes._\n\nThis mimics default Android functionality, where background music would stop for\na duration of a call or alarm and resume afterwards.\n\n# Usage\n\n## Install\n\n```powershell\npip install spotify-interlude\n```\n\n## Set up Spotify\nYou'll need to obtain a [Development Token](https://developer.spotify.com/) from Spotify.\n1. Start by [creating an account](https://accounts.spotify.com/en/status).\n2. Head to the [dashboard](https://developer.spotify.com/dashboard/applications) and create an App called Interlude on your account.\n3. Copy the client ID and secret. This package will need them to control your Spotify client.\n \n## Run Interlude\nStart Spotify and play some music. Then launch interlude:\n```powershell\n$Env:SPOTIFY_SECRET=...\n$ENV:SPOTIFY_CLIENT_ID=...\ninterlude\n```\nWhen you try to play some sounds in Chrome, the music should stop playing.\n\n## Configure interlude\n\nYou can tweak the behaviour of interlude using command line options:\n\n```powershell\ninterlude --help\n# Usage: interlude [OPTIONS]\n# \n#   Monitor the local Spotify client and apps making foreground noise. If\n#   --shortcut-path is specified, create a Windows shortcut with the same\n#   options instead.\n# \n# Options:\n#   --spotify-secret TEXT           Secret from your Spotify App dashboard.\n#                                   [env var: SPOTIFY_SECRET; required]\n#   --spotify-client-id TEXT        Client Id from your Spotify App dashboard.\n#                                   [env var: SPOTIFY_CLIENT_ID; required]\n#   -p, --process-name TEXT         Names of the programs which should pause\n#                                   Spotify when palying sound.  [default:\n#                                   chrome.exe, firefox.exe, Telegram.exe]\n#   -d, --device-name TEXT          Name of the Spotify device, in case you have\n#                                   multiple connected simultaneously. This can\n#                                   be used to pause palyback outside of this\n#                                   computer.  [default: SURFACE]\n#   --session-refresh-interval FLOAT\n#                                   How often to scan for new foreground apps\n#                                   (seconds)  [default: 5.0]\n#   --warmup-duration FLOAT         Delay between end of foreground sound and\n#                                   playback resume.  [default: 2.0]\n#   --shortcut-path PATH            Path where a shortcut to Interlude should be\n#                                   created.\n#   --log-path PATH                 Write logs to this file instead of stdout\n#   --log-level TEXT                Minimal level of the logs to display\n#                                   [default: INFO]\n#   --install-completion [bash|zsh|fish|powershell|pwsh]\n#                                   Install completion for the specified shell.\n#   --show-completion [bash|zsh|fish|powershell|pwsh]\n#                                   Show completion for the specified shell, to\n#                                   copy it or customize the installation.\n#   --help                          Show this message and exit.\n```\n\n## Create shortcut\nTo easily start interlude, create a shortcut with your desired settings:\n```powershell\ninterlude --shortcut-path ~/Desktop/Interlude.lnk # add other options as needed\n```\nNote: the Spotify secret and client ID will be baked into the shortcut.\n\n## Environment file\n\nThe CLI parses environment variables, so you can keep secrets etc. out of command line history.\n\nYou may find a [dotenv file loader](https://github.com/rajivharris/Set-PsEnv) handy in PowerShell.\n",
    'author': 'Hubert Bereś',
    'author_email': 'h.beres@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Ddedalus/spotify-interlude',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
