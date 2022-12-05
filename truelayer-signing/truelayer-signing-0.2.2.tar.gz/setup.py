# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['truelayer_signing']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT[crypto]>=2.3.0,<3.0.0']

setup_kwargs = {
    'name': 'truelayer-signing',
    'version': '0.2.2',
    'description': 'Produce & verify TrueLayer API requests signatures',
    'long_description': '# truelayer-signing\n\nPython package to produce & verify TrueLayer API requests signatures.\n\n## Install\n```\npip install truelayer-signing\n```\n\n## Generating a signature\n\n```python\ntl_signature = sign_with_pem(KID, PRIVATE_KEY) \\\n    .set_method(HttpMethod.POST) \\\n    .set_path(path) \\\n    .add_header("Idempotency-Key", idempotency_key) \\\n    .set_body(body) \\\n    .sign()\n```\nSee [full example](./examples/sign-request/).\n\n## Verifying webhooks\nThe `verify_with_jwks` function may be used to verify webhook `Tl-Signature` header signatures.\n\n```python\n# `jku` field is included in webhook signatures\njws_header = extract_jws_header(webhook_signature).jku\n\n# check `jku` is an allowed TrueLayer url & fetch jwks JSON (not provided by this lib)\nensure_jku_allowed(jku)\njwks = fetch_jwks(jku)\n\n# jwks may be used directly to verify a signature\nverify_with_jwks(jwks, jws_header) \\\n    .set_method(HttpMethod.POST) \\\n    .set_path(path) \\\n    .add_headers(headers) \\\n    .set_body(body) \\\n    .verify(tl_signature)\n```\n\nSee [webhook server example](./examples/webhook-server/).\n',
    'author': 'tl-flavio-barinas',
    'author_email': 'flavio.barinas@truelayer.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TrueLayer/truelayer-signing/tree/main/python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
