import os
from io import BytesIO
import json
from json import dumps, loads
import requests
from werkzeug import wrappers
import urllib

def fill_request_content(request, url, method, **kwargs):
    parsed_result = urllib.parse.urlparse(url)
    request_content = {
        'url': url,
        'method': method
    }
    if parsed_result.scheme:
        request_content['scheme'] = parsed_result.scheme
    if parsed_result.netloc:
        request_content['netloc'] = parsed_result.netloc
    if parsed_result.path:
        request_content['path'] = parsed_result.path
    if parsed_result.params:
        request_content['args'] = parsed_result.params
    if parsed_result.query:
        request_content['query'] = parsed_result.query
    if parsed_result.fragment:
        request_content['fragment'] = parsed_result.fragment
    if parsed_result.hostname:
        request_content['hostname'] = parsed_result.hostname
    if parsed_result.port:
        request_content['port'] = parsed_result.port
    if 'headers' in kwargs and kwargs.get('headers', None):
        request_content['headers'] = kwargs.get('headers')

    for key, value in request_content.items():
        setattr(request, key, value)

    return request

class MockPredictInputRetriever():
    @staticmethod
    def get(url, params = None, **kwargs):
        r"""Construct the request of predict API on proxy.

        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response

        Usage: the request argument is useful while implementing the predict function.
        """
        request = wrappers.Request.from_values(url)
        request = fill_request_content(request, url, 'GET', params = params)
        return request

    @staticmethod
    def post(url, data = None, json = None, **kwargs):
        r"""Retrieve the input argument of preprocess function as sending a POST request to the url.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Request <werkzeug.wrappers.Request>` object
        :rtype: werkzeug.wrappers.Request

        Usage: the request argument is useful while implementing the predict function.
        """

        # read files data first to avoid empty content issue
        files_data = None
        if 'files' in kwargs:
            files = kwargs.get('files')
            files_data = (b"")
            for _file in files:
                if files_data:
                    files_data += (b"\r\n")
                files_data += (b"--boundary\r\n")
                files_data += (b'Content-Disposition: form-data; name="') + _file.encode() + (b'"; filename="') + files.get(_file).name.encode() + (b'"\r\n')
                files_data += (b"\r\n")
                files_data += files.get(_file).read()
                files_data += (b"\r\n")
                files_data += (b"--boundary--")

        if 'files' in kwargs:
            request = wrappers.Request.from_values(
                data = data,
                json = json,
                input_stream = BytesIO(files_data),
                content_length = len(files_data),
                content_type = "multipart/form-data; boundary=boundary",
            )
            headers = {
                'Content-Length': len(files_data),
                'Content-Type': "multipart/form-data; boundary=boundary"
            }
            request = fill_request_content(request, url, 'POST', headers = headers)
        else:
            request = wrappers.Request.from_values(url, data = data, json = json)
            request = fill_request_content(request, url, 'POST')

        return request

    @staticmethod
    def put(url, data = None, **kwargs):
        r"""Retrieve the input argument of preprocess function as sending a PUT request to the url.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Request <werkzeug.wrappers.Request>` object
        :rtype: werkzeug.wrappers.Request

        Usage: the request argument is useful while implementing the predict function.
        """

        # read files data first to avoid empty content issue
        files_data = None
        if 'files' in kwargs:
            files = kwargs.get('files')
            files_data = (b"")
            for _file in files:
                if files_data:
                    files_data += (b"\r\n")
                files_data += (b"--boundary\r\n")
                files_data += (b'Content-Disposition: form-data; name="') + _file.encode() + (b'"; filename="') + files.get(_file).name.encode() + (b'"\r\n')
                files_data += (b"\r\n")
                files_data += files.get(_file).read()
                files_data += (b"\r\n")
                files_data += (b"--boundary--")

        if 'files' in kwargs:
            request = wrappers.Request.from_values(
                data = data,
                input_stream = BytesIO(files_data),
                content_length = len(files_data),
                content_type = "multipart/form-data; boundary=boundary",
            )
            headers = {
                'Content-Length': len(files_data),
                'Content-Type': "multipart/form-data; boundary=boundary"
            }
            request = fill_request_content(request, url, 'PUT', headers = headers)
        else:
            request = wrappers.Request.from_values(url, data = data)
            request = fill_request_content(request, url, 'POST')

        return request

class MockCVATInvokeInputRetriever(MockPredictInputRetriever):
    pass
