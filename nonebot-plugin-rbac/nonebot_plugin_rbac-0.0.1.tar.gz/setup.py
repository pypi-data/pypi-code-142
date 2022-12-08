# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nonebot_plugin_ac_demo']

package_data = \
{'': ['*']}

install_requires = \
['aiosqlite>=0.17.0,<0.18.0',
 'nonebot2>=2.0.0rc1,<3.0.0',
 'sqlalchemy[asyncio]>=1.4.42,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-rbac',
    'version': '0.0.1',
    'description': '',
    'long_description': '<!-- markdownlint-disable MD033 MD036 MD041 -->\n\n<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\nnonebot-plugin-access-control\n============\n\n_✨ Nonebot 权限控制 ✨_\n\n</div>\n\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/ssttkkl/nonebot-plugin-access-control/master/LICENSE">\n    <img src="https://img.shields.io/github/license/ssttkkl/nonebot-plugin-access-control.svg" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-access-control">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-access-control.svg" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">\n</p>\n\n## 特点\n\n- [x] 支持**功能级别**的细粒度权限控制\n- [x] 对未适配插件也支持**插件级别**的权限控制\n- [ ] 支持对权限开关等事件进行监听\n\n## 使用\n\n### 主体\n\n#### 概念\n\n让我们从一个例子引入：QQ上群组G的用户U发送了一条消息，该用户同时具有“用户U”、“群组G成员”、“QQ用户”、“Bot用户”这几个身份。同时QQ上群组G的用户V也发送了一条消息，该用户该用户同时具有“用户V”、“群组G成员”、“QQ用户”、“Bot用户”这几个身份。\n\n如果我们希望对用户进行权限控制，我们可以直接针对“用户U”、“用户V”这个级别分别配置权限。但我们希望对群组进行权限控制时，对群组内的每一个用户都分别配置权限，就有点力不从心了。我们希望能够直接针对“群组G”这个级别进行配置，而无需关心群组内都有什么成员。\n\n我们定义**主体（Subject）为用户所具有的身份，也是设置权限的基本单位。**\n\n一个用户通常拥有多个主体。回到上面的例子，第一位用户拥有“用户U”、“群组G成员”、“QQ用户”、“Bot用户”这四个主体；第二位用户拥有“用户V”、“群组G成员”、“QQ用户”、“Bot用户”这四个主体。用户拥有的所有主体，按照规模从小到大排序，呈现如下图的逐层包含关系：\n\n![](docs/img/1.svg)\n\n当设置权限时，我们直接针对一个主体进行设置。当鉴权时，我们对用户的所有主体按规模从小到大的顺序（下文将此顺序称为优先级顺序），逐一检查是否设置了权限。一旦检查到某个主体设置了权限，就以该主体设置的权限作为该用户的权限。\n\n回到上面的例子，假设我们对主体”群组G“禁用服务，但是对主体”用户V“启用服务。则在群组G内的用户U内将无法使用服务，但是则在群组G内的用户V可以使用。\n\n#### 应用\n\n在实际应用中，我们用一个字符串表示主体。并且我们约定，`all`表示所有用户，`<协议名>`表示所有此协议的用户，除此之外的所有主体均以`<协议名>:`开头。\n\n在OneBot协议中，每个用户所拥有的主体如下表所定义：\n\n| 主体                 | 含义       | 示例               | 必定存在             |\n|--------------------|----------|------------------|------------------|\n| onebot:<user_id>   | 用户ID     | onebot:12345678  | 是                |\n| onebot:g<group_id> | 群组ID     | onebot:g87654321 | 仅当消息来自群组或临时会话时存在 |\n| onebot             | OneBot用户 | onebot           | 是                |\n| all                | 所有用户     | all              | 是                |\n\n目前仅实现了OneBot协议。如果你能帮助我们进行其他协议适配，欢迎提交PR。\n\n### 服务\n\n服务（Service）为一组能够进行权限控制的功能的集合。服务可以拥有子服务，通过树结构组织服务，统一管理权限。\n\n整个插件就是一个服务（PluginService）。当插件未进行适配时，该插件只具有一个PluginService。\n\n若需要对插件进行适配，则需要从PluginService创建SubService，为插件的Matcher等功能入口应用SubService。（参考下文插件适配章节）\n\n### 指令\n\n进行权限开关的指令为`/ac`，仅超级用户可用。（通过在配置文件中设置`SUPERUSERS`变量可设置超级用户）\n\n- `/ac subject <主体> allow <服务>`：为主体启用服务\n- `/ac subject <主体> deny <服务>`：为主体禁用服务\n- `/ac subject <主体> remove <服务>`：为主体删除服务权限配置\n- `/ac subject <主体> ls`：列出主体已配置的服务权限\n- `/ac service <服务> ls`：列出服务已配置的主体权限\n\n其中`<服务>`的格式如下：\n\n- `<插件名>`：对整个插件进行开关\n- `<插件名>.<子服务名>`：对插件内的某个子服务进行开关（需参照下文对插件进行配置）\n\n## 插件适配\n\n完整代码：[src/nonebot_plugin_ac_demo](src/nonebot_plugin_ac_demo)\n\n1. 创建一个名为nonebot_plugin_ac_demo的插件\n\n2. 通过create_plugin_service函数创建一个PluginServic实例（注意参数必须为插件包名）\n\n```python\nfrom nonebot import require\n\nrequire("nonebot_plugin_ac_demo")\n\nfrom nonebot_plugin_access_control.service import create_plugin_service\n\nplugin_service = create_plugin_service("nonebot_plugin_ac_demo")\n```\n\n3. 通过PluginService.create_subservice创建SubService实例。在创建Matcher时，将subservice传递至rule或permission参数中\n\n```python\ngroup1 = plugin_service.create_subservice("group1")\n\n\n@on_command(\'a\', rule=group1.create_subservice("a")).handle()\nasync def _(matcher: Matcher):\n    await matcher.send("a")\n\n\n@on_command(\'b\', rule=group1.create_subservice("b")).handle()\nasync def _(matcher: Matcher):\n    await matcher.send("b")\n\n\n@on_command(\'c\', rule=plugin_service.create_subservice("c")).handle()\nasync def _(matcher: Matcher):\n    await matcher.send("c")\n```\n\n插件服务的结构如下所示：\n\n![](docs/img/2.svg)\n\n4. 通过指令配置服务权限\n\n执行下面的指令后，所有用户将无法调用指令`/a`与`/b`\n\n```\n/ac subject all deny nonebot_plugin_ac_demo.group1\n```\n\n执行下面的指令后，用户12345678将无法调用指令`/a`\n\n```\n/ac subject onebot:12345678 deny nonebot_plugin_ac_demo.a\n```\n\n执行下面的指令后，群组87654321的所有用户将无法调用除`/c`以外的任何指令\n\n```\n/ac subject onebot:g87654321 deny nonebot_plugin_ac_demo\n/ac subject onebot:g87654321 allow nonebot_plugin_ac_demo.c\n```',
    'author': 'ssttkkl',
    'author_email': 'huang.wen.long@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ssttkkl/nonebot-plugin-rbac',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
