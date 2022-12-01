# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class MarginCurrencyPair(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'base': 'str',
        'quote': 'str',
        'leverage': 'int',
        'min_base_amount': 'str',
        'min_quote_amount': 'str',
        'max_quote_amount': 'str',
        'status': 'int',
    }

    attribute_map = {
        'id': 'id',
        'base': 'base',
        'quote': 'quote',
        'leverage': 'leverage',
        'min_base_amount': 'min_base_amount',
        'min_quote_amount': 'min_quote_amount',
        'max_quote_amount': 'max_quote_amount',
        'status': 'status',
    }

    def __init__(
        self,
        id=None,
        base=None,
        quote=None,
        leverage=None,
        min_base_amount=None,
        min_quote_amount=None,
        max_quote_amount=None,
        status=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, int, str, str, str, int, Configuration) -> None
        """MarginCurrencyPair - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._base = None
        self._quote = None
        self._leverage = None
        self._min_base_amount = None
        self._min_quote_amount = None
        self._max_quote_amount = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if base is not None:
            self.base = base
        if quote is not None:
            self.quote = quote
        if leverage is not None:
            self.leverage = leverage
        if min_base_amount is not None:
            self.min_base_amount = min_base_amount
        if min_quote_amount is not None:
            self.min_quote_amount = min_quote_amount
        if max_quote_amount is not None:
            self.max_quote_amount = max_quote_amount
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this MarginCurrencyPair.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The id of this MarginCurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MarginCurrencyPair.

        Currency pair  # noqa: E501

        :param id: The id of this MarginCurrencyPair.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def base(self):
        """Gets the base of this MarginCurrencyPair.  # noqa: E501

        Base currency  # noqa: E501

        :return: The base of this MarginCurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this MarginCurrencyPair.

        Base currency  # noqa: E501

        :param base: The base of this MarginCurrencyPair.  # noqa: E501
        :type: str
        """

        self._base = base

    @property
    def quote(self):
        """Gets the quote of this MarginCurrencyPair.  # noqa: E501

        Quote currency  # noqa: E501

        :return: The quote of this MarginCurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this MarginCurrencyPair.

        Quote currency  # noqa: E501

        :param quote: The quote of this MarginCurrencyPair.  # noqa: E501
        :type: str
        """

        self._quote = quote

    @property
    def leverage(self):
        """Gets the leverage of this MarginCurrencyPair.  # noqa: E501

        Leverage  # noqa: E501

        :return: The leverage of this MarginCurrencyPair.  # noqa: E501
        :rtype: int
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this MarginCurrencyPair.

        Leverage  # noqa: E501

        :param leverage: The leverage of this MarginCurrencyPair.  # noqa: E501
        :type: int
        """

        self._leverage = leverage

    @property
    def min_base_amount(self):
        """Gets the min_base_amount of this MarginCurrencyPair.  # noqa: E501

        Minimum base currency to loan, `null` means no limit  # noqa: E501

        :return: The min_base_amount of this MarginCurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._min_base_amount

    @min_base_amount.setter
    def min_base_amount(self, min_base_amount):
        """Sets the min_base_amount of this MarginCurrencyPair.

        Minimum base currency to loan, `null` means no limit  # noqa: E501

        :param min_base_amount: The min_base_amount of this MarginCurrencyPair.  # noqa: E501
        :type: str
        """

        self._min_base_amount = min_base_amount

    @property
    def min_quote_amount(self):
        """Gets the min_quote_amount of this MarginCurrencyPair.  # noqa: E501

        Minimum quote currency to loan, `null` means no limit  # noqa: E501

        :return: The min_quote_amount of this MarginCurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._min_quote_amount

    @min_quote_amount.setter
    def min_quote_amount(self, min_quote_amount):
        """Sets the min_quote_amount of this MarginCurrencyPair.

        Minimum quote currency to loan, `null` means no limit  # noqa: E501

        :param min_quote_amount: The min_quote_amount of this MarginCurrencyPair.  # noqa: E501
        :type: str
        """

        self._min_quote_amount = min_quote_amount

    @property
    def max_quote_amount(self):
        """Gets the max_quote_amount of this MarginCurrencyPair.  # noqa: E501

        Maximum borrowable amount for quote currency. Base currency limit is calculated by quote maximum and market price. `null` means no limit  # noqa: E501

        :return: The max_quote_amount of this MarginCurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._max_quote_amount

    @max_quote_amount.setter
    def max_quote_amount(self, max_quote_amount):
        """Sets the max_quote_amount of this MarginCurrencyPair.

        Maximum borrowable amount for quote currency. Base currency limit is calculated by quote maximum and market price. `null` means no limit  # noqa: E501

        :param max_quote_amount: The max_quote_amount of this MarginCurrencyPair.  # noqa: E501
        :type: str
        """

        self._max_quote_amount = max_quote_amount

    @property
    def status(self):
        """Gets the status of this MarginCurrencyPair.  # noqa: E501

        Currency pair status   - `0`: disabled  - `1`: enabled  # noqa: E501

        :return: The status of this MarginCurrencyPair.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MarginCurrencyPair.

        Currency pair status   - `0`: disabled  - `1`: enabled  # noqa: E501

        :param status: The status of this MarginCurrencyPair.  # noqa: E501
        :type: int
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarginCurrencyPair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarginCurrencyPair):
            return True

        return self.to_dict() != other.to_dict()
