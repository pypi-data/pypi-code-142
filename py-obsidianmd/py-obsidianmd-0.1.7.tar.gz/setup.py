# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyomd', 'pyomd.config']

package_data = \
{'': ['*']}

install_requires = \
['python-frontmatter>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'py-obsidianmd',
    'version': '0.1.7',
    'description': 'python library for ObsidianMD',
    'long_description': '# py-obsidianmd\n\nA python library for modifying [Obsidian](https://obsidian.md/) notes in batch.\n\nSee the [full documentation](https://selimrbd.github.io/py-obsidianmd/)\n\n:warning: **Consider backing up your vault** before using the library, to avoid any risk of data loss.\n\n\n## Presentation video\n\n[![Watch the video](https://img.youtube.com/vi/gRPBAKiu37Y/hqdefault.jpg)](https://www.youtube.com/watch?v=gRPBAKiu37Y)\n\n## Quickstart\n\n```bash\npip install py-obsidianmd\n```\n\n```python\nfrom pathlib import Path\nfrom pyomd import Notes\nfrom pyomd.metadata import MetadataType\n\npath_dir = Path(\'/path/to/obsidian/folder\')\nnotes = Notes(path_dir)\n```\n\nYou can test the library on this [example vault](https://github.com/selimrbd/example-vault)\n\n## move metadata between frontmatter and inline\n\n```python\nnotes.metadata.move(fr=MetadataType.FRONTMATTER, to=MetadataType.INLINE)\nnotes.update_content(inline_inplace=False, inline_position="top", inline_tml="standard") #type: ignore\nnotes.write()\n```\n![](./docs/docs/assets/example-gifs/pyomd-1.gif)\n\n## regroup inline metadata inside a callout\n\n```python\nnotes.update_content(inline_inplace=False, inline_position="top", inline_tml="callout") #type: ignore\nnotes.write()\n```\n![](./docs/docs/assets/example-gifs/pyomd-2.gif)\n\n## add and remove metadata \n```python\nnotes.filter(has_meta=[("tags", "type/book", MetadataType.INLINE)])\n\nnotes.metadata.add(k="type", l="[[book]]", meta_type=MetadataType.INLINE)\nnotes.metadata.remove(k="tags", l="type/book", meta_type=MetadataType.INLINE)\n\nnotes.update_content(inline_inplace=False, inline_position="top", inline_tml="callout") #type: ignore\nnotes.write()\n```\n![](./docs/docs/assets/example-gifs/pyomd-3.gif)\n\n## License\n\n[BSD 3](LICENSE.txt)\n\n## Contributing\nContributions are welcome ! Different ways you can contribute:\n- **Write an issue**: report a bug, suggest an enhancement, ...\n- **Submit a pull request** to solve an open issue\n\nFor more details, see the [contribution guidelines](CONTRIBUTING.md).\n\n## Support\n\nIf you found this library useful and wish to support it\'s development, you can do so using the links below (paypal or Ko-fi). Thanks a bunch !\n\n<a href="https://www.paypal.com/donate/?hosted_button_id=R5NYTS46CQMSS"><img src="./docs/docs/assets/donate-paypal.png" width="150" height="100" /></a>\n<br>\n<a href="https://ko-fi.com/selimrbd"><img src="./docs/docs/assets/donate-kofi.png" width="200" height="50" /></a>',
    'author': 'Selim Raboudi',
    'author_email': 'selim.raboudi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/selimrbd/py-obsidianmd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
