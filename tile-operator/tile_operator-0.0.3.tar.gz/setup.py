# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tile_operator']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.0,<9.0.0',
 'geopandas>=0.12.0,<0.13.0',
 'matplotlib>=3.6.0,<4.0.0',
 'numpy>=1.23.0,<2.0.0',
 'pillow>=9.3.0,<10.0.0',
 'rasterio>=1.3.0,<2.0.0',
 'requests>=2.28.0,<3.0.0',
 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'tile-operator',
    'version': '0.0.3',
    'description': 'Tile Operation tool',
    'long_description': '# tile-operator\n\n## usage\n\n### CLI\n\n#### tile download\n\n```bash\n$ python to.py -v download https://tile.openstreetmap.jp/{z}/{x}/{y}.png tests/data/test.geojson 18\n\nTile Download\n\n Options:\n  tile_url=https://tile.openstreetmap.jp/{z}/{x}/{y}.png\n  file_path=tests/data/test.geojson\n  zoom_level=18\n\n\n100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:05<00:00,  5.11it/s]\n```\n\n#### help\n\n```bash\n$ python to.py --help        \nUsage: to.py [OPTIONS] COMMAND [ARGS]...\n\n  Tile operator v0.0.1\n\nOptions:\n  --version                 Show the version and exit.\n  -v, --verbose             verbose mode\n  --help                    Show this message and exit.\n\nCommands:\n  operate  Tile Operation\n```\n\n### python\n\n- install\n\n```bash\n$ pip install tile-operator\n```\n\n```python\nfrom tile_operator.operate import TileOperate\n\nto = TileOperate(\n    tile_url="https://tile.openstreetmap.jp/{z}/{x}/{y}.png",\n    file_path="tests/data/test.geojson",\n    zoom_level=18,\n)\nto.set_tile_list()\nto.download_all_tiles()\n```\n\n## test\n\n```bash\n$ pytest -qs tests\n```\n\n## development\n\n### setup\n\n```bash\n$ poetry config virtualenvs.in-project true\n$ pyenv global 3.9 # Version 3.7 or higher will work, but 3.9 is recommended.\n$ python -m venv .venv\n$ source .venv/bin/activate\n$ python -m pip install --upgrade pip\n$ poetry install\n$ poetry shell\n```\n\n### publish\n\n```bash\n$ poetry build\n$ poetry publish\n```\n',
    'author': 'nokonoko1203',
    'author_email': 'nokonoko.1203.777@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
