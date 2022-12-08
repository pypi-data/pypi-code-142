import requests

from metamask_institutional.sdk.bitgo.bitgo_create_tx_params import BitgoCreateTxParams
from metamask_institutional.sdk.bitgo.bitgo_list_response import BitgoListResponse
from metamask_institutional.sdk.bitgo.bitgo_response import BitgoResponse
from metamask_institutional.sdk.bitgo.bitgo_transaction import BitgoTransaction
from metamask_institutional.sdk.common.abstract_client import AbstractClient
from metamask_institutional.sdk.utils.inject_from_ import inject_from_on_all


class BitgoClient(AbstractClient):

    def __get_headers(self):
        """Internal method that creates the HTTP header to use for the calls against Cactus Custody's API. It includes an authorization header that uses the access token.

        Returns:
            The HTTP header as a dictionary.
        """
        return {
            "Content-Type": "application/json",
            "Authorization": 'Bearer ' + self.token
        }

    def get_transaction_by_custodian_tx_id(self, custodian_tx_id) -> BitgoListResponse[BitgoTransaction]:
        url = f"{self.api_url}/eth/wallets/transactions/{custodian_tx_id}"
        headers = self.__get_headers()

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise requests.HTTPError(
                f"Couldn't get the transaction. Request failed with status {response.status_code}: {response.json()}")

        # Parse response and build the result
        response_json = response.json()

        data_with_from_ = inject_from_on_all(response_json["data"])
        transactions = list(map(lambda json: BitgoTransaction(**json), data_with_from_))
        meta = response_json["_meta"]

        return BitgoListResponse(data=transactions, meta=meta)

    def create_transaction(self, wallet_id: str, tx_params: BitgoCreateTxParams) -> BitgoResponse[BitgoTransaction]:
        url = f"{self.api_url}/eth/wallet/{wallet_id}/tx/build"
        headers = self.__get_headers()
        payload = tx_params.dict(by_alias=True)
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 201:
            raise requests.HTTPError(
                f"Couldn't create the transaction. Request failed with status {response.status_code}: {response.json()}")

        # Parse and return
        response_json = response.json()
        return BitgoResponse[BitgoTransaction](**response_json)
