from typing import Union, Dict

import requests

from ..util import is_id
from ..system import LayerProfile, read_layer_profile
from ..universe import load_universe, Universe


class ServiceClient:

    def __init__(self, url='https://api.vyze.io/service', timeout=300):
        self._url = url
        self._token: Union[str, None] = None
        self._timeout = timeout
        self._universes: Dict[str, Universe] = {}
        self._universe: Universe | None = None

    def set_token(self, token: Union[str, None]) -> None:
        self._token = token

    def resolve_universe(self, name: str) -> str:
        u = self._build_url(f'resolve/universe', {'i': name})
        return self.__get(u)

    def get_layer_profile(self, profile_id: str) -> Union[LayerProfile, None]:
        u = self._build_url(f'profile/{profile_id}/tokens')
        layer_profile_str = self.__get(u, 'text')
        return read_layer_profile(layer_profile_str)

    def load_universe(self, univ: str) -> Union[Universe, None]:
        universe = self._universes.get(univ)
        if universe:
            return universe

        universe_id = None
        if is_id(univ):
            universe_id = univ
        else:
            universe = load_universe(univ)

        if not universe:
            if not universe_id:
                universe_id = self.resolve_universe(univ)

            if not universe_id:
                return None

            u = self._build_url(f'universe/{universe_id}/export', {'o': '1'})
            universe_def = self.__get(u, 'bytes')
            universe = load_universe(universe_def)

        if not universe:
            return None

        self._universes[universe.name] = universe
        self._universe = universe
        return universe

    @property
    def universe(self):
        return self._universe

    def _build_url(self, endpoint: str, params: Union[dict, None] = None):
        if params:
            return f'{self._url}/v1/{endpoint}?{"&".join([k + "=" + v for k, v in params.items()])}'
        return f'{self._url}/v1/{endpoint}'

    def __get(self, url: str, return_type: str = 'json') -> any:
        resp = requests.get(url, headers=self._get_headers(), timeout=self._timeout)
        if resp.status_code >= 300:
            raise RuntimeError(resp.text)
        if return_type == 'json':
            return resp.json()
        elif return_type == 'text':
            return resp.text
        elif return_type == 'bytes':
            return resp.content

    def _post(self, url: str, data: any) -> any:
        resp = requests.post(url, json=data, headers=self._get_headers(), timeout=self._timeout)
        return resp.json()

    def _put(self, url: str, data: any) -> any:
        resp = requests.put(url, json=data, headers=self._get_headers(), timeout=self._timeout)
        return resp.json()

    def _delete(self, url: str) -> any:
        resp = requests.delete(url, headers=self._get_headers(), timeout=self._timeout)
        return resp.json()

    def _get_headers(self, headers=None):
        if not headers:
            headers = {}
        if self._token:
            headers['Authorization'] = f'Bearer {self._token}'
        return headers
