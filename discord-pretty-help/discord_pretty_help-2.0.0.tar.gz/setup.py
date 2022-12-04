# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pretty_help']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['emoji = tests.test_pretty_help:run_emoji',
                     'run = tests.test_pretty_help:run']}

setup_kwargs = {
    'name': 'discord-pretty-help',
    'version': '2.0.0',
    'description': 'And nicer looking interactive help menu for discord.py',
    'long_description': '![version](https://img.shields.io/pypi/v/discord-pretty-help) ![python](https://img.shields.io/badge/python-3.8+-blue)\n\n# discord-pretty-help\n\nAn embed version of the built in help command for discord.py\n\n\n\nInspired by the DefaultHelpCommand that discord.py uses, but revised for embeds and additional sorting on individual pages that can be "scrolled" through. \n\n## Installation\n\n`pip install discord-pretty-help`\n\n## Usage\n\nExample of how to use it:\n\n```python\nfrom discord.ext import commands\nfrom pretty_help import PrettyHelp\n\nbot = commands.Bot(command_prefix="!", help_command=PrettyHelp())\n```\n\n\n\n### Added Optional Args\n\n- `color` - Set the default embed color\n- `delete_invoke` - Delete the message that invoked the help command. Requires message delete permission. Defaults is `False`\n- `ending_note` - Set the footer of the embed. Ending notes are fed a `commands.Context` (`ctx`) and a `PrettyHelp` (`help`) instance for more advanced customization.\n- `image_url` - The url of the image to be used on the embed\n- `index_title` - Set the index page name default is *"Categories"*\n- `menu` - The menu to use for navigating pages. Uses a `pretty_help.PrettyMenu()` instance. Default is `pretty_help.AppMenu()`\n- `no_category` - Set the name of the page with commands not part of a category. Default is "*No Category*"\n- `sort_commands` - Sort commands and categories alphabetically\n- `show_index` - Show the index page or not\n- `thumbnail_url` - The url of the thumbnail to be used on the emebed\n\n## Menus\n\n### pretty_help.EmojiMenu \n- Uses Emojis to navigate\n- `active_time` - Set the time (in seconds) that the message will be active. Default is 30s\n- `delete_after_timeout` - Delete the message after `active_time` instead of removing reactions. Default `False`\n- `page_left` - The emoji to use to page left\n- `page_right` - The emoji to use to page right\n- `remove` - The emoji to use to remove the help message\n\n![example](/images/example-emoji.gif)\n\n### pretty_help.AppMenu\n- Uses Application Interactions (buttons) for navigating\n- `timeout` - The duration the interaction will be active for. Defaults to `None`.\n- `ephemeral` - Send as an ephemeral message. Defaults to `False`.\n\n![example](/images/example-app.gif)\n\nBy default, the help will just pick a random color on every invoke. You can change this using the `color` argument:\n\n### Example of using a different menu and customization:\n\n```python\n\nfrom discord.ext import commands\nfrom pretty_help import EmojiMenu, PrettyHelp\n\n# ":discord:743511195197374563" is a custom discord emoji format. Adjust to match your own custom emoji.\nmenu = EmojiMenu(page_left="\\U0001F44D", page_right="👎", remove=":discord:743511195197374563", active_time=5)\n\n# Custom ending note\nending_note = "The ending note from {ctx.bot.user.name}\\nFor command {help.clean_prefix}{help.invoked_with}"\n\nbot = commands.Bot(command_prefix="!")\n\nbot.help_command = PrettyHelp(menu=menu, ending_note=ending_note)\n```\n\nThe basic `help` command will break commands up by cogs. Each cog will be a different page. Those pages can be navigated. \n\n![example](/images/example.gif)\n\n\n# Changelog\n\n## [2.0.0]\n - Subcommands in pages are indicated with a 🔗, previously it was unclear they were sub commands of the page title\n - Support Application commands\n - Support for GroupCogs\n - Navigation using discord interactions eg. Buttons and select menus \n\n\n# Notes:\n- discord.py must already be installed to use this\n- `manage-messages` permission is recommended so reactions can be removed automatically\n\n## Forks for other discord.py based libraries (maintanance not monitored):\n* [nextcord-pretty-help](https://github.com/squigjess/nextcord-pretty-help)',
    'author': 'StroupBSlayen',
    'author_email': '29642143+stroupbslayen@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/stroupbslayen/discord-pretty-help',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
