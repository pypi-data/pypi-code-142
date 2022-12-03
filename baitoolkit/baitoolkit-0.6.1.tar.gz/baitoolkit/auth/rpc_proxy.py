# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import typing
from urllib.parse import urlencode

import requests

from baitoolkit.auth.auth_constant import AuthConstant
from baitoolkit.common import logger_factory, type_util
from baitoolkit.exception.assert_util import assert_required
from baitoolkit.exception.errors import RpcError
from baitoolkit.web import blueprint
from baitoolkit.web.blueprint import JsonRtn
from baitoolkit.web.web_constant import WebConstant


class RpcProxy(object):
    """Remote proc call using auth head."""

    __logger = logger_factory.get_logger(__name__)

    class Method(object):

        def __init__(self, client_app_id: str, client_app_static_token, server_address: str, path: str):
            self._client_app_id = client_app_id
            self._client_app_static_token = client_app_static_token
            self._server_address = server_address
            self._path = path

        def __call__(self, authorization, method: str = WebConstant.HTTP_METHOD_GET,
                     path_data=None, body_data: object = None, header_data=None,
                     timeout=AuthConstant.RPC_CALL_TIMEOUT) -> typing.Any:
            """
            Call restful api.
            :param str authorization: The authorization will be verified by server.
            :param str method: request method of restful api.
            :param dict path_data: the parameters after ? in url.
            :param object body_data: (optional) Dictionary, list of tuples, bytes, or file-like
                                    object to send in the request body.
            :param dict header_data: data in http headers.
            :Return Any object if json response else class<Response> object
            """
            assert_required(authorization, 'authorization')
            url = self.build_url(self._path, path_data)
            headers = self.build_headers(authorization, header_data)

            def is_json(res):
                return True if WebConstant.HTTP_CONTENT_TYPE in res.headers and res.headers[
                    WebConstant.HTTP_CONTENT_TYPE] == WebConstant.HTTP_CONTENT_TYPE_JSON else False

            try:
                response = requests.request(method, url, headers=headers, data=body_data, timeout=timeout)
                if not is_json(response):
                    return response
                rtn = JsonRtn.construct(response)
            except BaseException as e:
                RpcProxy.logger.error('Failed to call %s due to %s' % (url, str(e)))
                raise RpcError(self._app_id, self._path, str(e))
            else:
                if rtn.code != WebConstant.SUCCESS_CODE:
                    raise RpcError(self._app_id, self._path, rtn.message, code=rtn.code, data=rtn.data)
                return rtn.data

        def build_url(self, path: str, path_data=None) -> str:
            url = blueprint.url_join(self._server_address, path)
            if path_data is not None:
                url = '%s?%s' % (url, urlencode(path_data))
            return url

        @staticmethod
        def build_headers(authorization, **kwargs) -> typing.Dict:
            if kwargs is None:
                return dict()
            headers = dict()
            headers[AuthConstant.AUTH_HEAD_NAME] = authorization
            type_util.dict_merge(headers, kwargs)
            return headers

    def __init__(self, client_app_id, client_app_static_token, server_address):
        """
        :param str client_app_id: the app id to call remote proc.
        :param str client_app_static_token: the app static token to call remote proc.
        """
        self._client_app_id = client_app_id
        self._client_app_static_token = client_app_static_token
        self._server_address = server_address

    def __getitem__(self, path):
        """
        :param str path: the remote rest api path, such as /abc/defG
        """
        return self.Method(self._client_app_id, self._client_app_static_token, self._server_address, path)

    def __getattr__(self, path):
        """
        :param str path: using __bs1__ to define /, such as the real path is abc/defG,
        the argument path should be abc__bs1__defG
        """
        path = path.replace("__bs1__", "/")
        return self.__getitem__(path)
