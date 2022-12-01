# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gate_api.api_client import ApiClient
from gate_api.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class FlashSwapApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_flash_swap_currencies(self, **kwargs):  # noqa: E501
        """List all supported currencies in flash swap  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_flash_swap_currencies(async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: list[gate_api.FlashSwapCurrency]
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_flash_swap_currencies_with_http_info(**kwargs)  # noqa: E501

    def list_flash_swap_currencies_with_http_info(self, **kwargs):  # noqa: E501
        """List all supported currencies in flash swap  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_flash_swap_currencies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(list[gate_api.FlashSwapCurrency], status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method list_flash_swap_currencies" % k
                )
            local_var_params[k] = v
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flash_swap/currencies',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FlashSwapCurrency]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def list_flash_swap_orders(self, **kwargs):  # noqa: E501
        """List all flash swap orders  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_flash_swap_orders(async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param int status: Flash swap order status  `1` - success `2` - failure
        :param str sell_currency: Currency to sell which can be retrieved from supported currency list API `GET /flash_swap/currencies`
        :param str buy_currency: Currency to buy which can be retrieved from supported currency list API `GET /flash_swap/currencies`
        :param bool reverse: If results are sorted by id in reverse order. Default to `true`  - `true`: sort by id in descending order(recent first) - `false`: sort by id in ascending order(oldest first)
        :param int limit: Maximum number of records to be returned in a single list
        :param int page: Page number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: list[gate_api.FlashSwapOrder]
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_flash_swap_orders_with_http_info(**kwargs)  # noqa: E501

    def list_flash_swap_orders_with_http_info(self, **kwargs):  # noqa: E501
        """List all flash swap orders  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_flash_swap_orders_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param int status: Flash swap order status  `1` - success `2` - failure
        :param str sell_currency: Currency to sell which can be retrieved from supported currency list API `GET /flash_swap/currencies`
        :param str buy_currency: Currency to buy which can be retrieved from supported currency list API `GET /flash_swap/currencies`
        :param bool reverse: If results are sorted by id in reverse order. Default to `true`  - `true`: sort by id in descending order(recent first) - `false`: sort by id in ascending order(oldest first)
        :param int limit: Maximum number of records to be returned in a single list
        :param int page: Page number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(list[gate_api.FlashSwapOrder], status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['status', 'sell_currency', 'buy_currency', 'reverse', 'limit', 'page']
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method list_flash_swap_orders" % k)
            local_var_params[k] = v
        del local_var_params['kwargs']

        if (
            self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `limit` when calling `list_flash_swap_orders`, must be a value less than or equal to `1000`"
            )  # noqa: E501
        if (
            self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `limit` when calling `list_flash_swap_orders`, must be a value greater than or equal to `1`"
            )  # noqa: E501
        if (
            self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `page` when calling `list_flash_swap_orders`, must be a value greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'sell_currency' in local_var_params and local_var_params['sell_currency'] is not None:  # noqa: E501
            query_params.append(('sell_currency', local_var_params['sell_currency']))  # noqa: E501
        if 'buy_currency' in local_var_params and local_var_params['buy_currency'] is not None:  # noqa: E501
            query_params.append(('buy_currency', local_var_params['buy_currency']))  # noqa: E501
        if 'reverse' in local_var_params and local_var_params['reverse'] is not None:  # noqa: E501
            query_params.append(('reverse', local_var_params['reverse']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiv4']  # noqa: E501

        return self.api_client.call_api(
            '/flash_swap/orders',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FlashSwapOrder]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def create_flash_swap_order(self, flash_swap_order_request, **kwargs):  # noqa: E501
        """Create a flash swap order  # noqa: E501

        Initiate a flash swap preview in advance because order creation requires a preview result  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_flash_swap_order(flash_swap_order_request, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param FlashSwapOrderRequest flash_swap_order_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: gate_api.FlashSwapOrder
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_flash_swap_order_with_http_info(flash_swap_order_request, **kwargs)  # noqa: E501

    def create_flash_swap_order_with_http_info(self, flash_swap_order_request, **kwargs):  # noqa: E501
        """Create a flash swap order  # noqa: E501

        Initiate a flash swap preview in advance because order creation requires a preview result  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_flash_swap_order_with_http_info(flash_swap_order_request, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param FlashSwapOrderRequest flash_swap_order_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(gate_api.FlashSwapOrder, status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['flash_swap_order_request']
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create_flash_swap_order" % k)
            local_var_params[k] = v
        del local_var_params['kwargs']
        # verify the required parameter 'flash_swap_order_request' is set
        if self.api_client.client_side_validation and (
            'flash_swap_order_request' not in local_var_params
            or local_var_params['flash_swap_order_request'] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `flash_swap_order_request` when calling `create_flash_swap_order`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'flash_swap_order_request' in local_var_params:
            body_params = local_var_params['flash_swap_order_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json']
        )  # noqa: E501

        # Authentication setting
        auth_settings = ['apiv4']  # noqa: E501

        return self.api_client.call_api(
            '/flash_swap/orders',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlashSwapOrder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_flash_swap_order(self, order_id, **kwargs):  # noqa: E501
        """Get a single flash swap order's detail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_flash_swap_order(order_id, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param int order_id: Flash swap order ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: gate_api.FlashSwapOrder
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_flash_swap_order_with_http_info(order_id, **kwargs)  # noqa: E501

    def get_flash_swap_order_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """Get a single flash swap order's detail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_flash_swap_order_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param int order_id: Flash swap order ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(gate_api.FlashSwapOrder, status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['order_id']
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_flash_swap_order" % k)
            local_var_params[k] = v
        del local_var_params['kwargs']
        # verify the required parameter 'order_id' is set
        if self.api_client.client_side_validation and (
            'order_id' not in local_var_params or local_var_params['order_id'] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `order_id` when calling `get_flash_swap_order`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_id' in local_var_params:
            path_params['order_id'] = local_var_params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiv4']  # noqa: E501

        return self.api_client.call_api(
            '/flash_swap/orders/{order_id}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlashSwapOrder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def preview_flash_swap_order(self, flash_swap_order_request, **kwargs):  # noqa: E501
        """Initiate a flash swap order preview  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.preview_flash_swap_order(flash_swap_order_request, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param FlashSwapOrderRequest flash_swap_order_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: gate_api.FlashSwapOrderPreview
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.preview_flash_swap_order_with_http_info(flash_swap_order_request, **kwargs)  # noqa: E501

    def preview_flash_swap_order_with_http_info(self, flash_swap_order_request, **kwargs):  # noqa: E501
        """Initiate a flash swap order preview  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.preview_flash_swap_order_with_http_info(flash_swap_order_request, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param FlashSwapOrderRequest flash_swap_order_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(gate_api.FlashSwapOrderPreview, status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['flash_swap_order_request']
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method preview_flash_swap_order" % k)
            local_var_params[k] = v
        del local_var_params['kwargs']
        # verify the required parameter 'flash_swap_order_request' is set
        if self.api_client.client_side_validation and (
            'flash_swap_order_request' not in local_var_params
            or local_var_params['flash_swap_order_request'] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `flash_swap_order_request` when calling `preview_flash_swap_order`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'flash_swap_order_request' in local_var_params:
            body_params = local_var_params['flash_swap_order_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json']
        )  # noqa: E501

        # Authentication setting
        auth_settings = ['apiv4']  # noqa: E501

        return self.api_client.call_api(
            '/flash_swap/orders/preview',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlashSwapOrderPreview',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
