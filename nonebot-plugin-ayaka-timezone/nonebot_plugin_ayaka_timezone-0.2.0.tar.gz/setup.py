# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

modules = \
['ayaka_timezone']
install_requires = \
['nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot-plugin-ayaka>=0.5.1,<0.6.0',
 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka-timezone',
    'version': '0.2.0',
    'description': '时区助手',
    'long_description': '# 时区助手 0.2.0\n\n基于[ayaka](https://github.com/bridgeL/nonebot-plugin-ayaka)开发的 时区助手 插件\n\n任何问题请发issue\n\n注意：只适用于群聊！\n\n## 安装插件\n\n`nb plugin install nonebot-plugin-ayaka-timezone`\n\n# 指令\n指令|参数|功能\n-|-|-\ntz_add|name, timezone|添加一条时区转换，例如，#tz_add 北京 8，#tz_add 伦敦 0，#tz_add 洛杉矶 -8\ntz|name|返回name对应时区的时间，例如 #tz 北京\ntz|number|返回对应时区的时间，例如 #tz 8\ntz_list|无|查看所有的时区转换\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-ayaka-timezone',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
