# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shabda']

package_data = \
{'': ['*'], 'shabda': ['templates/*']}

install_requires = \
['flask[async]',
 'freesound-api',
 'google-cloud-texttospeech',
 'gunicorn',
 'pydub',
 'requests',
 'termcolor',
 'typer[all]']

entry_points = \
{'console_scripts': ['shabda = shabda_cli:cli']}

setup_kwargs = {
    'name': 'shabda',
    'version': '0.1.0',
    'description': 'A semantic audio samples curator for livecoding software',
    'long_description': 'Shabda\n======\n\n![Shabda logo](assets/logo.png)\n\n\nShabda is a tool to fetch random samples from https://freesound.org/ based on given words, for use in impro sessions on instruments such as Tidal Cycles and Estuary.\n\n[Shabda](https://en.wikipedia.org/wiki/Shabda) is the Sanskrit word for "speech sound". In Sanskrit grammar, the term refers to an utterance in the sense of linguistic performance. \n\nInstall\n-------\n\n- Install Python 3: https://www.python.org/\n- Install pip: https://pypi.org/project/pip/\n- Install pipenv: `pip install pipenv`\n- Install dependencies: `pipenv install`\n- Install ffmpeg: https://ffmpeg.org/ (e.g. Debian/Ubuntu: `apt install ffmpeg`)\n\nUse (command line)\n------------------\n\nIn order to download a sample pack, execute in the terminal `pipenv run python shabda_cli.py <definition> --licenses <license_name>`.\n\nAny word can be a pack definition. If you want more than one sample, separate words by a comma: `blue,red`\n\nYou can define how many variations of a sample to assemble by adding a colon and a number.\ne.g. `blue,red:3,yellow:2` will produce one \'blue\' sample, three \'red\' samples and two \'yellow\' sample.\n\nThe optional `--licenses` parameter allows to fetch only samples that have the specified license. Multiple licenses can be allowed by repeating the `--licenses` argument. Possible licenses are `cc0` (Creative Commons Zero), `by` (Creative Commons Attribution), and `by-nc` (Creative Commons Attribution Non-Commercial).\n\nFull example:\n```\npipenv run python shabda_cli.py spaghetti:2,monster:4 --licenses cc0 --licenses by\n```\n\nUse (web application)\n---------------------\n\nLaunch the web application:\n\nIn debug mode:\n```\nFLASK_APP=shabda FLASK_DEBUG=1 pipenv run flask run\n```\nIn production:\n```\npipenv run gunicorn --workers=4 "shabda:create_app()" -b localhost:8000\n```\n\nTest\n----\n\n```\npipenv run pytest\n```\n\nNotes\n-----\n\nWith Estuary, Shabda makes use of this feature: https://github.com/dktr0/estuary/wiki#adding-sound-files-to-estuarywebdirt-on-the-fly\n\nTo do\n-----\n\n- Move all this to github issues or project :)\n- Explain how to launch on codespace / how to make port public\n- Change allowed duration in definition ?\n- List API and view\n- Solidify: Retry, Queue workers, queue status?\n  - https://huey.readthedocs.io/en/latest/index.html\n  - https://github.com/litements/litequeue\n  - (but with those there is no way to know a queue\'s status?)\n- Explain risks about throttling: https://freesound.org/docs/api/overview.html\n- Allow to rename sample ?\n  - Allow emojis in sample name ?\n  - Allow spaces in sample name ? special unicode spaces ? Reverse ?\n- Record your voice\n- Extract percussive ?\n  - https://librosa.org/doc/latest/generated/librosa.effects.hpss.html\n- Use advanced search in a funky way: https://freesound.org/docs/api/analysis_docs.html#analysis-docs\n- Fix refresh token method. Refresh regularly ?\n- Enforce all alpha minuscules and numbers in pack definition\n- Generate speech ;\n    - via external cli ? https://linuxhint.com/command-line-text-speech-apps-linux/\n    - via python lib ? https://pypi.org/project/pyttsx3/\n    - via TTS API? https://rapidapi.com/collection/best-text-to-speech-apis\n- Delete old samples (e.g. 7 days after last usage, note usage date)\n- Autorun pylint\n- Autorun pytest\n- Better cli interface (pack definition, licenses) \n- pip module\n  - Separate web/cli/core\n  - Finish migration from pipenv to Poetry\n  - Store freesound token in a predictable directory\n  - Store samples in a predictable directory (configurable)',
    'author': 'Alexandre G.-Raymond',
    'author_email': 'alex@ndre.gr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://shabda.ndre.gr/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
