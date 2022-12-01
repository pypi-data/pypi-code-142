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


class FuturesLiquidate(object):
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
        'time': 'int',
        'contract': 'str',
        'leverage': 'str',
        'size': 'int',
        'margin': 'str',
        'entry_price': 'str',
        'liq_price': 'str',
        'mark_price': 'str',
        'order_id': 'int',
        'order_price': 'str',
        'fill_price': 'str',
        'left': 'int',
    }

    attribute_map = {
        'time': 'time',
        'contract': 'contract',
        'leverage': 'leverage',
        'size': 'size',
        'margin': 'margin',
        'entry_price': 'entry_price',
        'liq_price': 'liq_price',
        'mark_price': 'mark_price',
        'order_id': 'order_id',
        'order_price': 'order_price',
        'fill_price': 'fill_price',
        'left': 'left',
    }

    def __init__(
        self,
        time=None,
        contract=None,
        leverage=None,
        size=None,
        margin=None,
        entry_price=None,
        liq_price=None,
        mark_price=None,
        order_id=None,
        order_price=None,
        fill_price=None,
        left=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (int, str, str, int, str, str, str, str, int, str, str, int, Configuration) -> None
        """FuturesLiquidate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._contract = None
        self._leverage = None
        self._size = None
        self._margin = None
        self._entry_price = None
        self._liq_price = None
        self._mark_price = None
        self._order_id = None
        self._order_price = None
        self._fill_price = None
        self._left = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if contract is not None:
            self.contract = contract
        if leverage is not None:
            self.leverage = leverage
        if size is not None:
            self.size = size
        if margin is not None:
            self.margin = margin
        if entry_price is not None:
            self.entry_price = entry_price
        if liq_price is not None:
            self.liq_price = liq_price
        if mark_price is not None:
            self.mark_price = mark_price
        if order_id is not None:
            self.order_id = order_id
        if order_price is not None:
            self.order_price = order_price
        if fill_price is not None:
            self.fill_price = fill_price
        if left is not None:
            self.left = left

    @property
    def time(self):
        """Gets the time of this FuturesLiquidate.  # noqa: E501

        Liquidation time  # noqa: E501

        :return: The time of this FuturesLiquidate.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this FuturesLiquidate.

        Liquidation time  # noqa: E501

        :param time: The time of this FuturesLiquidate.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def contract(self):
        """Gets the contract of this FuturesLiquidate.  # noqa: E501

        Futures contract  # noqa: E501

        :return: The contract of this FuturesLiquidate.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this FuturesLiquidate.

        Futures contract  # noqa: E501

        :param contract: The contract of this FuturesLiquidate.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def leverage(self):
        """Gets the leverage of this FuturesLiquidate.  # noqa: E501

        Position leverage. Not returned in public endpoints.  # noqa: E501

        :return: The leverage of this FuturesLiquidate.  # noqa: E501
        :rtype: str
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this FuturesLiquidate.

        Position leverage. Not returned in public endpoints.  # noqa: E501

        :param leverage: The leverage of this FuturesLiquidate.  # noqa: E501
        :type: str
        """

        self._leverage = leverage

    @property
    def size(self):
        """Gets the size of this FuturesLiquidate.  # noqa: E501

        Position size  # noqa: E501

        :return: The size of this FuturesLiquidate.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FuturesLiquidate.

        Position size  # noqa: E501

        :param size: The size of this FuturesLiquidate.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def margin(self):
        """Gets the margin of this FuturesLiquidate.  # noqa: E501

        Position margin. Not returned in public endpoints.  # noqa: E501

        :return: The margin of this FuturesLiquidate.  # noqa: E501
        :rtype: str
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this FuturesLiquidate.

        Position margin. Not returned in public endpoints.  # noqa: E501

        :param margin: The margin of this FuturesLiquidate.  # noqa: E501
        :type: str
        """

        self._margin = margin

    @property
    def entry_price(self):
        """Gets the entry_price of this FuturesLiquidate.  # noqa: E501

        Average entry price. Not returned in public endpoints.  # noqa: E501

        :return: The entry_price of this FuturesLiquidate.  # noqa: E501
        :rtype: str
        """
        return self._entry_price

    @entry_price.setter
    def entry_price(self, entry_price):
        """Sets the entry_price of this FuturesLiquidate.

        Average entry price. Not returned in public endpoints.  # noqa: E501

        :param entry_price: The entry_price of this FuturesLiquidate.  # noqa: E501
        :type: str
        """

        self._entry_price = entry_price

    @property
    def liq_price(self):
        """Gets the liq_price of this FuturesLiquidate.  # noqa: E501

        Liquidation price. Not returned in public endpoints.  # noqa: E501

        :return: The liq_price of this FuturesLiquidate.  # noqa: E501
        :rtype: str
        """
        return self._liq_price

    @liq_price.setter
    def liq_price(self, liq_price):
        """Sets the liq_price of this FuturesLiquidate.

        Liquidation price. Not returned in public endpoints.  # noqa: E501

        :param liq_price: The liq_price of this FuturesLiquidate.  # noqa: E501
        :type: str
        """

        self._liq_price = liq_price

    @property
    def mark_price(self):
        """Gets the mark_price of this FuturesLiquidate.  # noqa: E501

        Mark price. Not returned in public endpoints.  # noqa: E501

        :return: The mark_price of this FuturesLiquidate.  # noqa: E501
        :rtype: str
        """
        return self._mark_price

    @mark_price.setter
    def mark_price(self, mark_price):
        """Sets the mark_price of this FuturesLiquidate.

        Mark price. Not returned in public endpoints.  # noqa: E501

        :param mark_price: The mark_price of this FuturesLiquidate.  # noqa: E501
        :type: str
        """

        self._mark_price = mark_price

    @property
    def order_id(self):
        """Gets the order_id of this FuturesLiquidate.  # noqa: E501

        Liquidation order ID. Not returned in public endpoints.  # noqa: E501

        :return: The order_id of this FuturesLiquidate.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this FuturesLiquidate.

        Liquidation order ID. Not returned in public endpoints.  # noqa: E501

        :param order_id: The order_id of this FuturesLiquidate.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def order_price(self):
        """Gets the order_price of this FuturesLiquidate.  # noqa: E501

        Liquidation order price  # noqa: E501

        :return: The order_price of this FuturesLiquidate.  # noqa: E501
        :rtype: str
        """
        return self._order_price

    @order_price.setter
    def order_price(self, order_price):
        """Sets the order_price of this FuturesLiquidate.

        Liquidation order price  # noqa: E501

        :param order_price: The order_price of this FuturesLiquidate.  # noqa: E501
        :type: str
        """

        self._order_price = order_price

    @property
    def fill_price(self):
        """Gets the fill_price of this FuturesLiquidate.  # noqa: E501

        Liquidation order average taker price  # noqa: E501

        :return: The fill_price of this FuturesLiquidate.  # noqa: E501
        :rtype: str
        """
        return self._fill_price

    @fill_price.setter
    def fill_price(self, fill_price):
        """Sets the fill_price of this FuturesLiquidate.

        Liquidation order average taker price  # noqa: E501

        :param fill_price: The fill_price of this FuturesLiquidate.  # noqa: E501
        :type: str
        """

        self._fill_price = fill_price

    @property
    def left(self):
        """Gets the left of this FuturesLiquidate.  # noqa: E501

        Liquidation order maker size  # noqa: E501

        :return: The left of this FuturesLiquidate.  # noqa: E501
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this FuturesLiquidate.

        Liquidation order maker size  # noqa: E501

        :param left: The left of this FuturesLiquidate.  # noqa: E501
        :type: int
        """

        self._left = left

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
        if not isinstance(other, FuturesLiquidate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FuturesLiquidate):
            return True

        return self.to_dict() != other.to_dict()
