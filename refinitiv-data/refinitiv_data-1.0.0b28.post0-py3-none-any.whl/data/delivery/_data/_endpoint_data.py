# coding: utf8

import collections
from enum import Enum, unique
from typing import Any

Error = collections.namedtuple("Error", ["code", "message"])


@unique
class RequestMethod(str, Enum):
    """
    The RESTful Data service can support multiple methods when
    sending requests to a specified endpoint.
       GET : Request data from the specified endpoint.
       POST : Send data to the specified endpoint to create/update a resource.
       DELETE : Request to delete a resource from a specified endpoint.
       PUT : Send data to the specified endpoint to create/update a resource.
    """

    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)


class EndpointData(object):
    def __init__(self, raw: Any, **kwargs):
        if raw is None:
            raw = {}
        self._raw = raw
        self._kwargs = kwargs

    @property
    def raw(self):
        return self._raw
