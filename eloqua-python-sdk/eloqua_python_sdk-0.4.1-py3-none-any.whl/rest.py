import requests

from collections import OrderedDict
from eloquasdk.login import EloquaLogin
from eloquasdk.utils import b64auth

LOGIN_ENDPOINT = 'https://login.eloqua.com'
ID_ENDPOINT = LOGIN_ENDPOINT + '/id'
DEFAULT_API_VERSION = '2.0'


class EloquaRestClient(object):

    def __init__(self,
                 siteName=None,
                 username=None,
                 password=None,
                 client_id=None,
                 client_secret=None,
                 api_version=DEFAULT_API_VERSION):
        self.siteName = siteName
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_version = api_version

        if all(arg is not None for arg in (
                siteName, username, password,
                client_id, client_secret)):

            self.auth_type = 'oauth2'

            token_info = EloquaLogin(
                self.siteName,
                self.username,
                self.password,
                self.client_id,
                self.client_secret,
                self.auth_type)

            self.auth = ' '.join([token_info['token_type'],
                                 token_info['access_token']])

        elif all(arg is not None for arg in (
                siteName, username, password)):

            self.auth_type = 'basic'
            auth = 'Basic ' + b64auth(
                '\\'.join([siteName, username]), password)

            self.auth = auth.decode()

        else:
            raise TypeError(
                "You must provide login information"
            )

        self.headers = {
            'Authorization': self.auth,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        account_info = requests.get(ID_ENDPOINT, headers=self.headers)
        account_info = account_info.json(object_pairs_hook=OrderedDict)
        apis = account_info['urls']['apis']
        rest_url = apis['rest']['standard']

        self.base_url = rest_url.format(version=self.api_version)

    # Generic Rest function
    def restful(self, path, params=None, method='GET', **kwargs):
        url = self.base_url + path
        result = self._call_eloqua(method, url, params=params, **kwargs)

        json_result = result.json(object_pairs_hook=OrderedDict)

        if (len(json_result)) == 0:
            return None

        return json_result

    def _call_eloqua(self, method, url, **kwargs):
        result = requests.request(
            method, url, headers=self.headers, **kwargs)

        # TODO: handle exceptions

        return result
