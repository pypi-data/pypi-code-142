import requests
from .exceptions import SpackleException


class Customer:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def retrieve(customer_id, api_key=None, api_base=None):
        my_api_key = api_key
        if not my_api_key:
            from spackle import api_key

            my_api_key = api_key

        my_api_base = api_base
        if not my_api_base:
            from spackle import api_base

            my_api_base = api_base

        url = f"{my_api_base}/customers/{customer_id}/state"
        response = requests.get(url, headers={"Authorization": "Bearer " + my_api_key})
        data = response.json()

        if response.status_code != 200:
            raise SpackleException(data.get("error", "Unknown error"))

        return Customer(data)

    def enabled(self, key):
        for feature in self.data["features"]:
            if feature["name"] == key:
                return feature["value_enabled"]

        return False

    def limit(self, key):
        for feature in self.data["features"]:
            if feature["name"] == key:
                return feature["value_limit"]

        return 0
