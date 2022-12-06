from typing import Any, Dict, Tuple, Union

import requests

from invfinsdk.constants import API_PATH, API_VERSION


class Client:
    token: str

    def __init__(self, token: str) -> None:
        self.token = token

    def _base_build_url(self) -> str:
        return f"{API_PATH}{API_VERSION}/"

    def _build_request_params(
        self,
        path: str,
        params: Dict[str, Union[str, int]],
    ) -> Tuple[str, Dict[str, Union[str, int]]]:
        base_url = self._base_build_url()
        final_path = f"{base_url}{path}/"
        params.update({"api_key": self.token})
        return final_path, params

    def _perform_request(
        self,
        url: str,
        params: Dict[str, Union[str, int]],
    ) -> requests.Response:
        url, params = self._build_request_params(url, params)
        response = requests.get(url=url, params=params)
        response.raise_for_status()
        return response

    def _get_clean_response(
        self,
        url: str,
        params: Dict[str, Union[str, int]] = {},
    ) -> Dict[str, Any]:
        response = self._perform_request(url, params)
        return response.json()
