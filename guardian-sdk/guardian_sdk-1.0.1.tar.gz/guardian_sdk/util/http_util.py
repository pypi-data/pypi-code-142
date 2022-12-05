import urllib
from urllib import request
from urllib.error import HTTPError, URLError
from urllib.request import quote
from guardian_sdk.Request import Request
from guardian_sdk.Response import Response
from guardian_sdk.common import constant
from guardian_sdk.util import hmac256
from guardian_sdk.util import sign_builder
from guardian_sdk.util import utils
import logging
import ssl


def execute(req: Request):
    headers = _initBasicHeaders(req.get_app_key(), req.get_app_secret(), req.get_timeout(), req.get_method(),
                                req.get_host(),
                                req.get_path(), req.get_headers(), req.get_querys(), req.get_bodys(),
                                req.get_string_body(),
                                req.get_bytes_body(), req.get_sign_headers())
    for x in headers:
        logging.debug(f"{x}: {headers[x]}")
    try:
        url = req.get_host() + req.get_path() + _get_query_string(req.get_querys())
        url = quote(url, safe=";/?:@&=+$,", encoding="utf-8")
        logging.debug(f'url: {url}')

        data = None
        if req.get_bodys() is not None:
            data = urllib.parse.urlencode(req.get_bodys()).encode("utf-8")
        if req.get_bytes_body() is not None:
            data = req.get_bytes_body()
        if req.get_string_body() is not None and req.get_string_body() != "":
            data = req.get_string_body().encode("utf-8")

        http_req = request.Request(url, method=req.get_method(), data=data, headers=headers)

        context = ssl._create_unverified_context()

        http_resp = request.urlopen(http_req, timeout=req.get_timeout(), context=context)
        resp = Response(http_resp.getcode(), http_resp.headers.get(constant.HTTP_HEADER_CONTENT_TYPE),
                        None, http_req.headers, http_resp.read().decode())
        return resp
    except HTTPError as e:
        return Response(e.getcode(), e.headers.get(constant.HTTP_HEADER_CONTENT_TYPE),
                        e.headers.get(constant.X_GW_ERROR_MESSAGE), e.headers, e.read().decode())
    except URLError as e:
        return Response(500, None, None, None, e.reason)


def _get_query_string(querys={}):
    if not querys:
        return ""
    tmp_list = []
    for k in querys:
        if k:
            if len(tmp_list) > 0:
                tmp_list.append("&")
            tmp_list.append(k)
            if querys[k]:
                tmp_list.append("=")
                tmp_list.append(querys[k])
    tmp_list.insert(0, "?")
    return "".join(tmp_list)


def _initBasicHeaders(app_key,
                      app_secret,
                      timeout,
                      method,
                      host,
                      path,
                      headers={},
                      querys={},
                      bodys={},
                      string_body=None,
                      bytes_body=None,
                      sign_headers=None):
    headers[constant.X_GW_TIMESTAMP] = utils.get_timestamp()
    headers[constant.X_GW_NONCE] = utils.get_uuid()
    headers[constant.X_GW_KEY] = app_key
    headers[constant.X_GW_SIGNATURE] = hmac256.sign(
        sign_builder.build_string_to_sign(method, path, headers, querys, bodys, sign_headers),
        app_secret)

    return headers
