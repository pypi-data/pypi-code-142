import requests
import flask
from .common import convert_kwargs

class MockPredictInputRetriever():
    @staticmethod
    def get(url, params = None, **kwargs):
        r"""Construct the request of predict API on proxy.

        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Request <werkzeug.wrappers.Request>` object
        :rtype: werkzeug.wrappers.Request

        Usage: the request argument is useful while implementing the predict function.
        """
        converted_kwargs = convert_kwargs(**kwargs)
        request = flask.Request.from_values(url, query_string = params, method = "GET", **converted_kwargs)
        return request

    @staticmethod
    def post(url, data = None, json = None, **kwargs):
        r"""Construct the request of predict API on proxy.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Request <werkzeug.wrappers.Request>` object
        :rtype: werkzeug.wrappers.Request

        Usage: the request argument is useful while implementing the predict function.
        """

        converted_kwargs = convert_kwargs(**kwargs)
        request = flask.Request.from_values(url, data = data, json = json, method = "POST", **converted_kwargs)
        return request

    @staticmethod
    def put(url, data = None, **kwargs):
        r"""Construct the request of predict API on proxy.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Request <werkzeug.wrappers.Request>` object
        :rtype: werkzeug.wrappers.Request

        Usage: the request argument is useful while implementing the predict function.
        """

        converted_kwargs = convert_kwargs(**kwargs)
        request = flask.Request.from_values(url, data = data, method = "PUT", **converted_kwargs)
        return request

class MockCVATInvokeInputRetriever(MockPredictInputRetriever):
    pass
