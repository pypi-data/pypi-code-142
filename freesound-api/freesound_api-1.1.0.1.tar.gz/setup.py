# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['freesound']
install_requires = \
['requests>2.27,<3.0']

setup_kwargs = {
    'name': 'freesound-api',
    'version': '1.1.0.1',
    'description': 'A Python client for the Freesound APIv2. Clone of freesound-python.',
    'long_description': 'freesound.py\n============\n\nA Python client for the [Freesound](https://freesound.org) APIv2.\n\nThis is a cold fork of https://github.com/MTG/freesound-python for publishing on pypi\n\nFind the API documentation at http://www.freesound.org/docs/api/. \nApply for an API key at https://www.freesound.org/apiv2/apply/. \n\nThe client automatically maps function arguments to http parameters of the API. \nJSON results are converted to python objects, but are also available in their original form (JSON loaded into dictionaries) using the method `.as_dict()` of returned objets (see [examples file](https://github.com/ilesinge/freesound-api/blob/master/examples.py)). \nThe main object types (`Sound`, `User`, `Pack`) are augmented with the corresponding API calls.\n\nNote that POST resources are not supported. Downloading full quality sounds requires Oauth2 authentication (see https://freesound.org/docs/api/authentication.html). Oauth2 authentication is supported by passing an access token, but you are expected to implement the workflow to obtain that access token. Here is an [example implementation of the Freesound OAuth2 workflow using Flask](https://gist.github.com/ffont/3607ba4af9814f3877cd42894a564222).\n\nExample usage:\n\n```python\nimport freesound\n\nclient = freesound.FreesoundClient()\nclient.set_token("<your_api_key>","token")\n\nresults = client.text_search(query="dubstep",fields="id,name,previews")\n\nfor sound in results:\n    sound.retrieve_preview(".",sound.name+".mp3")\n    print(sound.name)\n\n```\n\n## Installation\n\n```\npip install freesound-api\n```\n\n## Advanced usage\n\n### Modifying the requests\' session:\n\nYou can easily extend/modify the way how requests are done by interacting directly with\nthe session object of the client.\n\nFor example, adding proxies:\n```python\nproxies = {\n  \'http\': \'http://10.10.1.10:3128\',\n  \'https\': \'http://10.10.1.10:1080\',\n}\nclient.session.proxies.update(proxies)\n```\n\nor adding [rate limiting](https://github.com/JWCook/requests-ratelimiter):\n```python\nfrom requests_ratelimiter import LimiterSession\n\n# Apply a rate-limit (59 requests per minute) to all requests\nclient.session = LimiterSession(per_minute=59)\n```\n\n### Authenticating with OAuth\nHere is an example authentication flow with the help of [Requests-OAuthlib](https://requests-oauthlib.readthedocs.io/).\n```python\nfrom requests_oauthlib import OAuth2Session\n\nimport freesound\n\nclient_id = "<your_client_id>"\nclient_secret = "<your_client_secret>"\n\n# do the OAuth dance\noauth = OAuth2Session(client_id)\n\nauthorization_url, state = oauth.authorization_url(\n    "https://freesound.org/apiv2/oauth2/authorize/"\n)\nprint(f"Please go to {authorization_url} and authorize access.")\n\nauthorization_code = input("Please enter the authorization code:")\noauth_token = oauth.fetch_token(\n    "https://freesound.org/apiv2/oauth2/access_token/",\n    authorization_code,\n    client_secret=client_secret,\n)\n\nclient = freesound.FreesoundClient()\nclient.set_token(oauth_token["access_token"], "oauth")\n```\n',
    'author': 'Universitat Pompeu Fabra',
    'author_email': 'None',
    'maintainer': 'Alexandre Gravel-Raymond',
    'maintainer_email': 'alex@ndre.gr',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
