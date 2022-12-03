# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['funcenter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'funcenter',
    'version': '1.1',
    'description': 'Some random functions I made... includes color formatting, text formatting, basic math, and most of all... dumb algorithms. Enjoy.',
    'long_description': '# Funcenter\n\nThis is a simple package. You can use it however you want! Please let me know if there are any errors.\n\n### Color/Text Formatting\nThis package offers some basic color and text formatting, in the form of:\n- bold(`str`), b(`str`)\n  - <span style="color:magenta">bold(\'str\')</span> --> **str**\n- italic(`str`), i(`str`)\n - <span style="color:magenta">italic(\'str\')</span> --> *str*\n- underline(`str`), underl(`str`), ul(`str`)\n - <span style="color:magenta">underline(\'str\')</span> --> <u>str</u>\n- format(`option`), color(`option`)\n  - Sets the format or color.\n- clear()\n  - Clears all formatting.\n- fprint(`option`, `str`), cprint(`option`, `str`)[^1]\n  - Print `str` in the format of `option`.\n  - <span style="color:magenta">fprint(\'bold, \'str\')</span> --> **str**\n\n### Printing\nSome simple printing functions.\n- println(`str`, `x`)\n  - Prints *`x`* new lines after the `str` (default is 1).\n- printsln(`str`)\n  - Print the following print statement on the same line as `str`.\n- printx(`str`, `x`)\n  - Print `str` *`x`* times. <span style="color:magenta">`printx(\'str\', 3)`</span> prints the following\n  \n    ```\n    str\n    str\n    str\n    ```\n- typewriter(`str`, `speed`)\n  - Print `str` character-by-character (typewriter-like effect) using `speed` *(from slowest to fastest: 1, 2, 3)*.\n  - **<span style="color:red">`DO NOT USE WITH ESCAPE CHARACTERS`</span>**\n\n### Math\nVery very minimal and basic:\n- isdecimal(`var`)\n  - Returns <span style="color:blue">`True`</span> if `var` is a decimal.\n- factorial(`num`)\n  - Returns the factorial of `num`\n\n### Other\n- check_similarity(`str1`, `str2`, `rating`, `debug`)[^1]\n- charsplit(`str`)\n  - Returns a <span style="color:blue">list</span> of each character in `str`.\n- uncharsplit(`list`)\n  - Exactly what it sounds like. The reverse of the above; Returns a <span style="color:blue">string</span> of `list`. And yes I know how easy this is. I wanted it.\n  \n[^1]: Work in progress. Use caution.',
    'author': 'uncenter',
    'author_email': 'uncenteristaken@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://uncenter.org/funcenter',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
