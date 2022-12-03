import requests
import logging
import json
from bind_sdk.requests_payload.debin_payload import DebinPayload
from bind_sdk.requests_payload.transfer_payload import TransferPayload

logger = logging.getLogger(__name__)

headers = {"content-type": "application/json"}


class BindService:
    @staticmethod
    def login(username: str, password: str, bind_endpoint: str) -> str:
        logger.info(f"username: {username} | password:{password}")

        url = f"{bind_endpoint}/login/jwt"

        payload = json.dumps({"username": f"{username}", "password": f"{password}"})

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    @staticmethod
    def bancked_cuit(
        cuit: str,
        bind_credential: str,
        bind_endpoint: str,
        obp_document_type: str = "cuit",
    ) -> dict:
        url = f"{bind_endpoint}/persons/{cuit}/banks"
        headers["Authorization"] = f"JWT :{bind_credential}"
        headers["obp_document_type"] = obp_document_type

        response = requests.request("GET", url, headers=headers)

        return response.json()

    @staticmethod
    def get_views(bind_credential: str, bind_endpoint: str, bank_id: int):
        url = f"{bind_endpoint}/banks/{bank_id}/accounts"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @staticmethod
    def get_accounts(
        bind_credential: str, bind_endpoint: str, bank_id: int, view_id: str
    ) -> dict:
        url = f"{bind_endpoint}/banks/{bank_id}/accounts/{view_id}"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @staticmethod
    def get_account(
        account_id: str,
        bind_credential: str,
        bind_endpoint: str,
        bank_id: int,
        view_id: str,
    ) -> dict:
        url = f"{bind_endpoint}/banks/{bank_id}/accounts/{account_id}/{view_id}"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @staticmethod
    def get_account_movements(
        account_id: str,
        bind_credential: str,
        bind_endpoint: str,
        bank_id: int,
        view_id: str,
    ) -> dict:
        url = f"{bind_endpoint}/banks/{bank_id}/accounts/{account_id}/{view_id}/transactions"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @staticmethod
    def get_account_by_alias(
        alias: str, bind_credential: str, bind_endpoint: str
    ) -> dict:
        url = f"{bind_endpoint}/accounts/alias/{alias}"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @staticmethod
    def get_account_by_cbu_cvu(
        cbu_cvu: int, bind_credential: str, bind_endpoint: str
    ) -> dict:
        url = f"{bind_endpoint}/accounts/cbu/{cbu_cvu}"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @staticmethod
    def send_transfer(
        payload: dict,
        account_id: str,
        bind_credential: str,
        bind_endpoint: str,
        bank_id: int,
        view_id: str,
    ) -> dict:
        url = f"{bind_endpoint}/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/TRANSFER/transaction-requests"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("POST", url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_transfers(
        account_id: str,
        bind_credential: str,
        bind_endpoint: str,
        bank_id: int,
        view_id: str,
    ) -> dict:
        url = f"{bind_endpoint}/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/TRANSFER"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @staticmethod
    def get_transfer(
        transfer_id: str,
        account_id: str,
        bind_credential: str,
        bind_endpoint: str,
        bank_id: int,
        view_id: str,
    ) -> dict:
        url = f"{bind_endpoint}/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/TRANSFER/{transfer_id}"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @staticmethod
    def send_debin(
        payload: dict,
        account_id: str,
        bind_credential: str,
        bind_endpoint: str,
        bank_id: int,
        view_id: str,
    ) -> dict:
        url = f"{bind_endpoint}/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/DEBIN/transaction-requests"
        headers["Authorization"] = f"JWT :{bind_credential}"
        response = requests.request("POST", url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_debins_by_status(
        status: str,
        account_id: str,
        bind_credential: str,
        bind_endpoint: str,
        bank_id: int,
        view_id: str,
    ) -> dict:
        url = f"{bind_endpoint}/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/DEBIN"
        headers["Authorization"] = f"JWT :{bind_credential}"
        headers["obp_status"] = status
        response = requests.request("GET", url, headers=headers)
        return response.json()
