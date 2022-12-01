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


class WithdrawalApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def withdraw(self, ledger_record, **kwargs):  # noqa: E501
        """Withdraw  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.withdraw(ledger_record, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param LedgerRecord ledger_record: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: gate_api.LedgerRecord
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.withdraw_with_http_info(ledger_record, **kwargs)  # noqa: E501

    def withdraw_with_http_info(self, ledger_record, **kwargs):  # noqa: E501
        """Withdraw  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.withdraw_with_http_info(ledger_record, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param LedgerRecord ledger_record: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(gate_api.LedgerRecord, status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['ledger_record']
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method withdraw" % k)
            local_var_params[k] = v
        del local_var_params['kwargs']
        # verify the required parameter 'ledger_record' is set
        if self.api_client.client_side_validation and (
            'ledger_record' not in local_var_params or local_var_params['ledger_record'] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ledger_record` when calling `withdraw`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ledger_record' in local_var_params:
            body_params = local_var_params['ledger_record']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json']
        )  # noqa: E501

        # Authentication setting
        auth_settings = ['apiv4']  # noqa: E501

        return self.api_client.call_api(
            '/withdrawals',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LedgerRecord',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def cancel_withdrawal(self, withdrawal_id, **kwargs):  # noqa: E501
        """Cancel withdrawal with specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_withdrawal(withdrawal_id, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param str withdrawal_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: gate_api.LedgerRecord
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_withdrawal_with_http_info(withdrawal_id, **kwargs)  # noqa: E501

    def cancel_withdrawal_with_http_info(self, withdrawal_id, **kwargs):  # noqa: E501
        """Cancel withdrawal with specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_withdrawal_with_http_info(withdrawal_id, async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param str withdrawal_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(gate_api.LedgerRecord, status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['withdrawal_id']
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method cancel_withdrawal" % k)
            local_var_params[k] = v
        del local_var_params['kwargs']
        # verify the required parameter 'withdrawal_id' is set
        if self.api_client.client_side_validation and (
            'withdrawal_id' not in local_var_params or local_var_params['withdrawal_id'] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `withdrawal_id` when calling `cancel_withdrawal`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'withdrawal_id' in local_var_params:
            path_params['withdrawal_id'] = local_var_params['withdrawal_id']  # noqa: E501

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
            '/withdrawals/{withdrawal_id}',
            'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LedgerRecord',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
