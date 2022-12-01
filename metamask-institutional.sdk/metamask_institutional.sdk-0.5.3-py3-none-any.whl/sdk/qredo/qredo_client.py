import requests

from metamask_institutional.sdk.common.abstract_client import AbstractClient
from metamask_institutional.sdk.qredo.qredo_new_transaction import QredoNewTransaction
from metamask_institutional.sdk.qredo.qredo_transaction_info import QredoTransactionInfo
from cachetools import TTLCache


class QredoClient(AbstractClient):

    def __init__(self, api_url, token):
        self.api_url = api_url
        self.token = token
        self.cache = TTLCache(maxsize=1, ttl=86400)  # Default TTL. The cache get re-created later with actual token expiry

    def __create_access_token(self):
        """Internal method that creates an access token, necessary to authenticate other calls against Qredo's API.

        Returns:
            The access token as a string.
        """
        url = self.api_url+'/connect/token'
        querystring = {"grant_type": "refresh_token",
                       "refresh_token": self.token}
        payload = ""

        response = requests.post(url, data=payload, params=querystring)
        if (response.status_code != 200):
            raise requests.HTTPError(
                f"Couldn't create the access token, {response.text}")

        response_json = response.json()
        access_token = response_json["access_token"]
        expires_in = response_json["expires_in"]
        return access_token, expires_in

    def __create_access_token_cached(self):
        """Lazily fetch the access token, looking up in the cache before. If the access is not in the cache, we fetch it then store it.
        Note that we have to dynamically re-recreate the cache after fetching the token, because the TTL we want to use is extracted from the token's expires_in.
        """
        if 'access_token' not in self.cache:
            access_token, expires_in = self.__create_access_token()
            self.cache = TTLCache(maxsize=1, ttl=expires_in)
            self.cache['access_token'] = access_token

        return self.cache['access_token']

    def __get_headers(self):
        """Returns the HTTP header to use in requests to the custodian"""
        access_token = self.__create_access_token_cached()
        return {
            "Content-Type": "application/json",
            "Authorization": 'Bearer ' + access_token
        }

    def get_transaction(self, tx_id: str) -> QredoTransactionInfo:
        url = self.api_url + '/connect/transaction/' + tx_id
        payload = ""
        headers = self.__get_headers()

        response = requests.get(url, data=payload, headers=headers)
        if (response.status_code != 200):
            raise requests.HTTPError(
                f"Couldn't get the transaction, {response.text}")

        # Parse response
        response_json = response.json()
        response_json["from_"] = response.json()["from"]

        return QredoTransactionInfo(**response_json)

    def create_transaction(self, new_transaction: QredoNewTransaction) -> QredoTransactionInfo:
        url = self.api_url + "/connect/transaction"
        headers = self.__get_headers()

        payload = new_transaction.dict()
        payload["from"] = payload["from_"]
        response = requests.post(url, json=payload, headers=headers)

        if (response.status_code != 200):
            raise requests.HTTPError(
                f"Couldn't create the transaction, {response.text}")

        # Parse response
        response_json = response.json()
        return QredoTransactionInfo(**response_json)
