# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wyvern',
 'wyvern.commands',
 'wyvern.components',
 'wyvern.constructors',
 'wyvern.extensions',
 'wyvern.gateway',
 'wyvern.interactions',
 'wyvern.models',
 'wyvern.rest',
 'wyvern.state_handlers']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'attrs>=22.1.0,<23.0.0']

setup_kwargs = {
    'name': 'wyvern',
    'version': '0.0.4a0',
    'description': 'A flexible and easy to use Discord API wrapper for python 🚀.',
    'long_description': '# wyvern\n\n<p align="center">\n<img src="https://raw.githubusercontent.com/sarthhh/wyvern/master/docs/assets/wyvern.png" height=150 width=150><br><br>\n<img src="https://img.shields.io/github/license/sarthhh/wyvern?style=flat-square">\n<img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square">\n<img src="https://img.shields.io/badge/%20type_checker-pyright-%231674b1?style=flat-square">\n<img src="https://img.shields.io/github/stars/sarthhh/wyvern?style=flat-square">\n<img src="https://img.shields.io/github/last-commit/sarthhh/wyvern?style=flat-square">\n<img src="https://img.shields.io/pypi/pyversions/wyvern?style=flat-square">\n<img src="https://img.shields.io/pypi/v/wyvern?style=flat-square">\n<br><br>\nA [WIP] flexible and easy to use Discord API wrapper for python 🚀.\n</p>\n\n> Warning: This library is very unstable and things might not work as expected. Feel free to create an issue.\n\n## Important Links\n\nSupport server: https://discord.gg/FyEE54u9GF\n\nDocumentation: https://sarthhh.github.io/wyvern/\n\nPYPI: https://pypi.org/projects/wyvern\n\n## Installation\n```sh\n$python -m pip install git+https://github.com/sarthhh/wyvern\n```\n\n## Example Code:\n\n* CommandsClient with commands support.\n```py\nimport wyvern\n\n# creating a CommandsClient object to interaction with commands.\nclient = wyvern.CommandsClient("TOKEN")\n\n# creating a slash command using with_slash_command decorator.\n@client.with_slash_command(name="hello", description="says a hello")\nasync def hello(interaction: wyvern.ApplicationCommandInteraction) -> None:\n    # creating a response to the interaction.\n    await interaction.create_message_response("hi!")\n\n\n# running the bot.\nclient.run()\n\n```\n* Basic GatewayClient with listener. \n```py\nimport wyvern\n\n# creating a GatewayClient instance and storing it into the client variable.\n# this acts as the interface between your bot and the code.\n\nclient = wyvern.GatewayClient("TOKEN", intents=wyvern.Intents.UNPRIVILEGED | wyvern.Intents.MESSAGE_CONTENT)\n\n# creating an EventListener object and adding it to the client\'s event handler using the\n# @client.listen decorator. You can set the maximum amount of time this listener will get triggered using\n# the `max_trigger kwarg in the listener decorator.`\n\n\n@client.as_listener(wyvern.Event.MESSAGE_CREATE)\nasync def message_create(message: wyvern.Message) -> None:\n    """This coroutine is triggerd whenever the MESSAGE_CREATE event gets dispatched."""\n    if message.content and message.content.lower() == "!ping":\n        await message.respond("pong!")\n\n\n# runs the bot.\n\nclient.run()\n```',
    'author': 'sarthhh',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
