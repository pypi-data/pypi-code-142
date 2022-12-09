import urllib
import requests
import flask
from .common import convert_kwargs

def convert_to_get_request_url(url):
    parsed_result = urllib.parse.urlparse(url)
    target_url = ''
    if parsed_result.scheme:
        target_url = "{}://".format(parsed_result.scheme)
    if parsed_result.netloc:
        target_url = "{}{}".format(target_url, parsed_result.netloc)
    target_url = "{}/get-request".format(target_url)
    if parsed_result.query:
        target_url = "{}?{}".format(target_url, parsed_result.query)

    return target_url

class PredictInputRetriever():
    @staticmethod
    def get(url, params = None, **kwargs):
        r"""Retrieve the request of predict API on proxy.

        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Request <werkzeug.wrappers.Request>` object
        :rtype: werkzeug.wrappers.Request

        Usage: the request argument is useful while implementing the predict function.
        """
        target_url = convert_to_get_request_url(url)
        converted_kwargs = convert_kwargs(**kwargs)

        response = requests.get(target_url, params = params, **kwargs)
        response = response.json()
        environ_base = response.pop('environ_base', None)
        if environ_base:
            converted_kwargs['environ_base'] = environ_base

        request = flask.Request.from_values(url, query_string = params, method = "GET", **converted_kwargs)
        return request

    @staticmethod
    def post(url, data = None, json = None, **kwargs):
        r"""Retrieve the request of predict API on proxy.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Request <werkzeug.wrappers.Request>` object
        :rtype: werkzeug.wrappers.Request

        Usage: the request argument is useful while implementing the predict function.
        """

        target_url = convert_to_get_request_url(url)
        converted_kwargs = convert_kwargs(**kwargs)

        response = requests.post(target_url, data = data, json = json, **kwargs)
        response = response.json()
        environ_base = response.pop('environ_base', None)
        if environ_base:
            converted_kwargs['environ_base'] = environ_base
        request = flask.Request.from_values(url, data = data, json = json, method = "POST", **converted_kwargs)
        return request

    @staticmethod
    def put(url, data = None, **kwargs):
        r"""Retrieve the request of predict API on proxy.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Request <werkzeug.wrappers.Request>` object
        :rtype: werkzeug.wrappers.Request

        Usage: the request argument is useful while implementing the predict function.
        """

        target_url = convert_to_get_request_url(url)
        converted_kwargs = convert_kwargs(**kwargs)

        response = requests.put(target_url, data = data, **kwargs)
        response = response.json()
        environ_base = response.pop('environ_base', None)
        if environ_base:
            converted_kwargs['environ_base'] = environ_base
        request = flask.Request.from_values(url, data = data, method = "PUT", **converted_kwargs)
        return request

class CVATInvokeInputRetriever(PredictInputRetriever):
    pass
