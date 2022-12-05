# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nonebot_plugin_majsoul',
 'nonebot_plugin_majsoul.interceptors',
 'nonebot_plugin_majsoul.network',
 'nonebot_plugin_majsoul.paifuya',
 'nonebot_plugin_majsoul.paifuya.data',
 'nonebot_plugin_majsoul.paifuya.data.models',
 'nonebot_plugin_majsoul.paifuya.mappers',
 'nonebot_plugin_majsoul.paifuya.parsers',
 'nonebot_plugin_majsoul.utils']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'icmplib>=3.0.3,<4.0.0',
 'monthdelta>=0.9.1,<0.10.0',
 'nonebot2>=2.0.0rc1,<3.0.0',
 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-majsoul',
    'version': '0.0.1',
    'description': '',
    'long_description': 'nonebot-plugin-majsoul\n========\n\n受[DaiShengSheng/Majsoul_bot](https://github.com/DaiShengSheng/Majsoul_bot)启发而写的雀魂信息查询 Bot 插件。\n\n## 功能\n\n### 雀魂牌谱屋\n\n- [x] 个人数据查询（可按照时间、按照场数、按照房间类型查询）\n- [ ] 个人最近对局查询\n\n## LICENSE\n\nAGPLv3\n',
    'author': 'ssttkkl',
    'author_email': 'huang.wen.long@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
