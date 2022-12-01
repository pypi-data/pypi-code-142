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


class CurrencyChain(object):
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
        'chain': 'str',
        'name_cn': 'str',
        'name_en': 'str',
        'is_disabled': 'int',
        'is_deposit_disabled': 'int',
        'is_withdraw_disabled': 'int',
    }

    attribute_map = {
        'chain': 'chain',
        'name_cn': 'name_cn',
        'name_en': 'name_en',
        'is_disabled': 'is_disabled',
        'is_deposit_disabled': 'is_deposit_disabled',
        'is_withdraw_disabled': 'is_withdraw_disabled',
    }

    def __init__(
        self,
        chain=None,
        name_cn=None,
        name_en=None,
        is_disabled=None,
        is_deposit_disabled=None,
        is_withdraw_disabled=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, int, int, int, Configuration) -> None
        """CurrencyChain - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._chain = None
        self._name_cn = None
        self._name_en = None
        self._is_disabled = None
        self._is_deposit_disabled = None
        self._is_withdraw_disabled = None
        self.discriminator = None

        if chain is not None:
            self.chain = chain
        if name_cn is not None:
            self.name_cn = name_cn
        if name_en is not None:
            self.name_en = name_en
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if is_deposit_disabled is not None:
            self.is_deposit_disabled = is_deposit_disabled
        if is_withdraw_disabled is not None:
            self.is_withdraw_disabled = is_withdraw_disabled

    @property
    def chain(self):
        """Gets the chain of this CurrencyChain.  # noqa: E501

        Chain name  # noqa: E501

        :return: The chain of this CurrencyChain.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this CurrencyChain.

        Chain name  # noqa: E501

        :param chain: The chain of this CurrencyChain.  # noqa: E501
        :type: str
        """

        self._chain = chain

    @property
    def name_cn(self):
        """Gets the name_cn of this CurrencyChain.  # noqa: E501

        Chain name in Chinese  # noqa: E501

        :return: The name_cn of this CurrencyChain.  # noqa: E501
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        """Sets the name_cn of this CurrencyChain.

        Chain name in Chinese  # noqa: E501

        :param name_cn: The name_cn of this CurrencyChain.  # noqa: E501
        :type: str
        """

        self._name_cn = name_cn

    @property
    def name_en(self):
        """Gets the name_en of this CurrencyChain.  # noqa: E501

        Chain name in English  # noqa: E501

        :return: The name_en of this CurrencyChain.  # noqa: E501
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this CurrencyChain.

        Chain name in English  # noqa: E501

        :param name_en: The name_en of this CurrencyChain.  # noqa: E501
        :type: str
        """

        self._name_en = name_en

    @property
    def is_disabled(self):
        """Gets the is_disabled of this CurrencyChain.  # noqa: E501

        If it is disabled. 0 means NOT being disabled  # noqa: E501

        :return: The is_disabled of this CurrencyChain.  # noqa: E501
        :rtype: int
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this CurrencyChain.

        If it is disabled. 0 means NOT being disabled  # noqa: E501

        :param is_disabled: The is_disabled of this CurrencyChain.  # noqa: E501
        :type: int
        """

        self._is_disabled = is_disabled

    @property
    def is_deposit_disabled(self):
        """Gets the is_deposit_disabled of this CurrencyChain.  # noqa: E501

        Is deposit disabled. 0 means not  # noqa: E501

        :return: The is_deposit_disabled of this CurrencyChain.  # noqa: E501
        :rtype: int
        """
        return self._is_deposit_disabled

    @is_deposit_disabled.setter
    def is_deposit_disabled(self, is_deposit_disabled):
        """Sets the is_deposit_disabled of this CurrencyChain.

        Is deposit disabled. 0 means not  # noqa: E501

        :param is_deposit_disabled: The is_deposit_disabled of this CurrencyChain.  # noqa: E501
        :type: int
        """

        self._is_deposit_disabled = is_deposit_disabled

    @property
    def is_withdraw_disabled(self):
        """Gets the is_withdraw_disabled of this CurrencyChain.  # noqa: E501

        Is withdrawal disabled. 0 means not  # noqa: E501

        :return: The is_withdraw_disabled of this CurrencyChain.  # noqa: E501
        :rtype: int
        """
        return self._is_withdraw_disabled

    @is_withdraw_disabled.setter
    def is_withdraw_disabled(self, is_withdraw_disabled):
        """Sets the is_withdraw_disabled of this CurrencyChain.

        Is withdrawal disabled. 0 means not  # noqa: E501

        :param is_withdraw_disabled: The is_withdraw_disabled of this CurrencyChain.  # noqa: E501
        :type: int
        """

        self._is_withdraw_disabled = is_withdraw_disabled

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
        if not isinstance(other, CurrencyChain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrencyChain):
            return True

        return self.to_dict() != other.to_dict()
