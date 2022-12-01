# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['weblogin']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.9.1,<5.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'weblogin',
    'version': '1.1',
    'description': 'Automates logging into web UIs to access unofficial APIs',
    'long_description': 'We want to use APIs from web UIs that require login. What we want to do\nis to set up a session, login and then use the API of the page. The\nreason we want to do this is to use existing APIs. For instance, the\nuser group management service at KTH, see\n[1](#UGEditor){reference-type="ref" reference="UGEditor"}. We can then\nuse the service, track the requests in the browser\'s developer tools.\nThen we can simply make the same requests from Python.\n\n![Screenshot of the KTH UG Editor with Firefox\'s Developer Tools open,\nshowing network requests made.](https://github.com/dbosk/weblogin/raw/main/doc/figs/ug.png){#UGEditor width="\\\\columnwidth"}\n\nFor instance, we can redo the request in\n[1](#UGEditor){reference-type="ref" reference="UGEditor"} like this:\n\n``` {.python}\nfrom weblogin.kth import AutologinSession\nimport os\n\nug = AutologinSession(os.environ["KTH_LOGIN"],\n                      os.environ["KTH_PASSWD"],\n                      "https://app.kth.se/ug-gruppeditor/")\n\nresponse = ug.get("https://app.kth.se/ug-gruppeditor/api/ug/users"\n                  "?filter=memberOf eq \'u26yk1i3\'")\n```\n\nThe code above will access the API used by the KTH UG group editor\nservice. It will automatically sign in when needed. The API URLs don\'t\ntrigger a redirect to log in, they just give a 401 unauthorized error.\nHowever, we can use the main URL to the UI to trigger such an event, log\nin and then access the API. All this happens automatically in the\nbackground.\n\nThe way we do this is to subclass the `requests.Session` class to\nintercept all requests of a session to check for signs indicating that\nwe must log in. When we detect such sign, we log in and resume as if\nnothing ever happened.\n',
    'author': 'Daniel Bosk',
    'author_email': 'dbosk@kth.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dbosk/weblogin',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
