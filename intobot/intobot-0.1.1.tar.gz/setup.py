# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['intobot']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'vkbottle>=4.3.12,<5.0.0']

setup_kwargs = {
    'name': 'intobot',
    'version': '0.1.1',
    'description': 'A tool to make every script into a VK bot. Better than `every_script_is_a_vk_bot`, because `intobot` can serve multiple users simultaneously.',
    'long_description': '# intobot\n\nThis tool can turn your script into a VK bot. In every script launched with this tool, `input` and `print` will work with chats instead of the console. A script is ran one time for every user who writes to the bot. First message from a user starts the script execution and cannot be received from the script.\n\nInstallation:\n\n    pip install intobot\n\nUse it like this:\n\n    python -m intobot -t [token_file_name.txt] [script_name].py\n\nEverything above that is in brackets needs to be filled by you. (Brackets should be omitted.)\n\nWhen the script ends, the user is not served anymore, so to serve the user infinitely, add an infinite loop to the script. This was made to allow better flexibility and make it as close to console execution of scripts as possible.\n\n[Predecessor: every_script_is_a_vk_bot](https://github.com/megahomyak/every_script_is_a_vk_bot)\n',
    'author': 'megahomyak',
    'author_email': 'g.megahomyak@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
