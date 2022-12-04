# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['hashdecrypt']
install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'hashdecrypt',
    'version': '1.0.1',
    'description': 'Decrypt Metamask, Brawe, Ronin, BinanceChain vault data via Python',
    'long_description': '# HashDecrypt 1.0.0\n\n[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)\n\nDecryptor cold wallets data, from extension Metamask, Ronin, Binance, Brawe, etc.\n\n- Decrypt vault data\n- Return mnemonic , derivation key, description\n- Many options\n\n\n\n## Installation\n\nPython requires [Python.org](https://www.python.org/) v.3.7\n\nInstall the dependencies and devDependencies and start the server.\n\n```sh\napt update && apt upgrade\napt install python3 && apt install python3-pip\npip3 install HashDecrypt \n```\n> Note: `Example hash\\vault to decrypt`\n\n```sh\n{"data": "M5YTg9f1PP62HlCyuX1l2Bq+OnwgvjhoVc+FklxWqBSeHg4ihGypUjUtS5T3M/MHPsh5GATR/iKzdvhHdFGm5moqqhITU5RTZUuqDOdy2MOZh++moX/vwgyUiz9HS9OPb0Y5su4FGu2emhEw8X7Eb0kfOCCt8Q8iNjR8lHCQPHStiupd/MA05lV48bC/INStN7nDr1WDa+0TFpNGmVE9KeQe9xBtBm4Uw/JFWXZ9r12dua2DURkczPvqNrftxohPRmszYZ83psGSMpAAWqWcLzal3TOCZElB6SdFTLxBO9G1NXPC+u8vig+nxwPJKhBSkRvVqHOe4ncjkCjVM55+S7/J0QE9c/EAZS47WXOHRg+579UYPW79onmJkH9i6/F6NHU/FfMrzGmqlPys9kRp4eLfpqpnxOj72E1sdHodSfgksE6EzK1C6k5naQGOqIInPjllKP5tBi+oap8iLiFFGp87DMvvSnkdDyPfc42XxFemJa63/GTinTUzR6Klg1aC5RCJS8fyk24VUnH2zSIWZNgdqC8P49P5lWqXCN6Tkysf5sgGLoSwxrAHFJmUDLZEZajRCQe/6yzbuOfbg7hqubWco/J+EO1AwrwvhsoBwtX6QTZqF9jManWLqAslogAiaWmZeOxNjXdYpF1Q5cy4IDOS5miv7Xz+hGnB4lUSBN9VZz+cdJrVBNM3Xa5HDkS+fzGzMa95oG2obXnWvQrm1Ct1+kclt+jG7jGeLkc6XwxYgLabHGc0wSAVMLhNYB9Mk+97", "iv": "6CD2HmS+Zu32dz4BMbyICg==", "salt": "TkHQ2jqz2CYYbeAasJTJJX4oU+LoXstTdRxefxaSC/g="}\n```\n> Note: `Example python code:`\n\n```python\nfrom hashDecrypt import hdec\nVAULT = \'{"data": "M5YT....9Mk+97", "iv": "6CD2Hm...Cg==", "salt": "TkHQ....xaSC/g="}\'\nPASSWORD = "Awerawer22"\nw = hdec()\nobj = w.decrypt(PASSWORD, VAULT)\nprint(obj)\n```\n\n\n## License\n\nMIT\n\n**Free Software, Hell Yeah!**\n\n[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn\'t be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)\n\n   [dill]: <https://github.com/joemccann/dillinger>\n   [git-repo-url]: <https://github.com/joemccann/dillinger.git>\n   [john gruber]: <http://daringfireball.net>\n   [df1]: <http://daringfireball.net/projects/markdown/>\n   [markdown-it]: <https://github.com/markdown-it/markdown-it>\n   [Ace Editor]: <http://ace.ajax.org>\n   [node.js]: <http://nodejs.org>\n   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>\n   [jQuery]: <http://jquery.com>\n   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>\n   [express]: <http://expressjs.com>\n   [AngularJS]: <http://angularjs.org>\n   [Gulp]: <http://gulpjs.com>\n\n   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>\n   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>\n   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>\n   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>\n   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>\n   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>\n',
    'author': 'M16',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
