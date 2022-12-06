# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_gpt']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'nonebot-adapter-onebot>=2.1.5,<3.0.0',
 'nonebot2>=2.0.0-rc.1,<3.0.0',
 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-gpt',
    'version': '0.1.5',
    'description': 'Chatbot plugin based on ChatGPT for Nonebot.',
    'long_description': '# nonebot-plugin-gpt\n\n一个调用 `ChatGPT` 的聊天插件，它可以为不同的群聊分别保存聊天状态。\n\n这意味着，不同的群聊之间，聊天记录的上下文都是**相互独立**的。\n\n## 安装\n\n+ 使用 `pip` 安装：\n  \n  ```bash\n  pip install -U nonebot-plugin-gpt\n  ```\n\n\n## 配置项\n\n关于如何配置，请参考 [Nonebot 文档](https://v2.nonebot.dev/docs/tutorial/configuration#%E9%85%8D%E7%BD%AE%E6%96%B9%E5%BC%8F)。\n\n+ `GPT_SESSION_TOKEN`: 在 [https://chat.openai.com/chat](https://chat.openai.com/chat) 下，把 `F12` -> `Application` -> `Cookies` -> `__Secure-next-auth.session-token` 的内容复制下来，填入此配置项。\n+ `GPT_API_KEY`：到 [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys) 生成你的 `API Key`，填入此配置项。\n+ `GPT_SUDOERS`：一个有权限控制此机器人的QQ号列表，例如`[123, 456]`。\n+ `GPT_PROBABILITY`：回复普通消息的概率，默认为 `0`，也就是不回复。我觉得这个功能其实不太好，但是考虑到某些人可能想要以这种方式与机器人互动，还是加上了这个配置项，并且必须你手动开启。\n\n\n## 使用\n\n+ `/gpt {message}`\n\n  聊天，这个没什么好介绍的。\n\n+ `/gpt_control {action}`\n\n  在 `GPT_SUDOERS` 中的用户可以控制此机器人，有下列两个`action`：\n\n  + `refresh_session`：刷新 `session`，根据 `ChatGPT` 下的 [issue #11](https://github.com/acheong08/ChatGPT/issues/11)，你填写的 `session` 应当有一个月的有效期。\n  + `reset_status`：刷新聊天记录的上下文。\n\n+ 当 `GPT_PROBABILITY` 不为 `0` 时，有概率回复你发的普通消息。但是如果没有文本，例如只发了图片或聊天记录，它是不会回复的。\n',
    'author': 'kifuan',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kifuan/nonebot-plugin-gpt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
