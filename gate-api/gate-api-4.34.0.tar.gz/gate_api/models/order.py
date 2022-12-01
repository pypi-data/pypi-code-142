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


class Order(object):
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
        'text': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'create_time_ms': 'int',
        'update_time_ms': 'int',
        'status': 'str',
        'currency_pair': 'str',
        'type': 'str',
        'account': 'str',
        'side': 'str',
        'amount': 'str',
        'price': 'str',
        'time_in_force': 'str',
        'iceberg': 'str',
        'auto_borrow': 'bool',
        'auto_repay': 'bool',
        'left': 'str',
        'fill_price': 'str',
        'filled_total': 'str',
        'fee': 'str',
        'fee_currency': 'str',
        'point_fee': 'str',
        'gt_fee': 'str',
        'gt_maker_fee': 'str',
        'gt_taker_fee': 'str',
        'gt_discount': 'bool',
        'rebated_fee': 'str',
        'rebated_fee_currency': 'str',
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_time_ms': 'create_time_ms',
        'update_time_ms': 'update_time_ms',
        'status': 'status',
        'currency_pair': 'currency_pair',
        'type': 'type',
        'account': 'account',
        'side': 'side',
        'amount': 'amount',
        'price': 'price',
        'time_in_force': 'time_in_force',
        'iceberg': 'iceberg',
        'auto_borrow': 'auto_borrow',
        'auto_repay': 'auto_repay',
        'left': 'left',
        'fill_price': 'fill_price',
        'filled_total': 'filled_total',
        'fee': 'fee',
        'fee_currency': 'fee_currency',
        'point_fee': 'point_fee',
        'gt_fee': 'gt_fee',
        'gt_maker_fee': 'gt_maker_fee',
        'gt_taker_fee': 'gt_taker_fee',
        'gt_discount': 'gt_discount',
        'rebated_fee': 'rebated_fee',
        'rebated_fee_currency': 'rebated_fee_currency',
    }

    def __init__(
        self,
        id=None,
        text=None,
        create_time=None,
        update_time=None,
        create_time_ms=None,
        update_time_ms=None,
        status=None,
        currency_pair=None,
        type='limit',
        account='spot',
        side=None,
        amount=None,
        price=None,
        time_in_force='gtc',
        iceberg=None,
        auto_borrow=None,
        auto_repay=None,
        left=None,
        fill_price=None,
        filled_total=None,
        fee=None,
        fee_currency=None,
        point_fee=None,
        gt_fee=None,
        gt_maker_fee=None,
        gt_taker_fee=None,
        gt_discount=None,
        rebated_fee=None,
        rebated_fee_currency=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, int, int, str, str, str, str, str, str, str, str, str, bool, bool, str, str, str, str, str, str, str, str, str, bool, str, str, Configuration) -> None
        """Order - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._text = None
        self._create_time = None
        self._update_time = None
        self._create_time_ms = None
        self._update_time_ms = None
        self._status = None
        self._currency_pair = None
        self._type = None
        self._account = None
        self._side = None
        self._amount = None
        self._price = None
        self._time_in_force = None
        self._iceberg = None
        self._auto_borrow = None
        self._auto_repay = None
        self._left = None
        self._fill_price = None
        self._filled_total = None
        self._fee = None
        self._fee_currency = None
        self._point_fee = None
        self._gt_fee = None
        self._gt_maker_fee = None
        self._gt_taker_fee = None
        self._gt_discount = None
        self._rebated_fee = None
        self._rebated_fee_currency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_time_ms is not None:
            self.create_time_ms = create_time_ms
        if update_time_ms is not None:
            self.update_time_ms = update_time_ms
        if status is not None:
            self.status = status
        self.currency_pair = currency_pair
        if type is not None:
            self.type = type
        if account is not None:
            self.account = account
        self.side = side
        self.amount = amount
        if price is not None:
            self.price = price
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if iceberg is not None:
            self.iceberg = iceberg
        if auto_borrow is not None:
            self.auto_borrow = auto_borrow
        if auto_repay is not None:
            self.auto_repay = auto_repay
        if left is not None:
            self.left = left
        if fill_price is not None:
            self.fill_price = fill_price
        if filled_total is not None:
            self.filled_total = filled_total
        if fee is not None:
            self.fee = fee
        if fee_currency is not None:
            self.fee_currency = fee_currency
        if point_fee is not None:
            self.point_fee = point_fee
        if gt_fee is not None:
            self.gt_fee = gt_fee
        if gt_maker_fee is not None:
            self.gt_maker_fee = gt_maker_fee
        if gt_taker_fee is not None:
            self.gt_taker_fee = gt_taker_fee
        if gt_discount is not None:
            self.gt_discount = gt_discount
        if rebated_fee is not None:
            self.rebated_fee = rebated_fee
        if rebated_fee_currency is not None:
            self.rebated_fee_currency = rebated_fee_currency

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501

        Order ID  # noqa: E501

        :return: The id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.

        Order ID  # noqa: E501

        :param id: The id of this Order.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this Order.  # noqa: E501

        User defined information. If not empty, must follow the rules below:  1. prefixed with `t-` 2. no longer than 28 bytes without `t-` prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)   # noqa: E501

        :return: The text of this Order.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Order.

        User defined information. If not empty, must follow the rules below:  1. prefixed with `t-` 2. no longer than 28 bytes without `t-` prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)   # noqa: E501

        :param text: The text of this Order.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def create_time(self):
        """Gets the create_time of this Order.  # noqa: E501

        Creation time of order  # noqa: E501

        :return: The create_time of this Order.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Order.

        Creation time of order  # noqa: E501

        :param create_time: The create_time of this Order.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Order.  # noqa: E501

        Last modification time of order  # noqa: E501

        :return: The update_time of this Order.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Order.

        Last modification time of order  # noqa: E501

        :param update_time: The update_time of this Order.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def create_time_ms(self):
        """Gets the create_time_ms of this Order.  # noqa: E501

        Creation time of order (in milliseconds)  # noqa: E501

        :return: The create_time_ms of this Order.  # noqa: E501
        :rtype: int
        """
        return self._create_time_ms

    @create_time_ms.setter
    def create_time_ms(self, create_time_ms):
        """Sets the create_time_ms of this Order.

        Creation time of order (in milliseconds)  # noqa: E501

        :param create_time_ms: The create_time_ms of this Order.  # noqa: E501
        :type: int
        """

        self._create_time_ms = create_time_ms

    @property
    def update_time_ms(self):
        """Gets the update_time_ms of this Order.  # noqa: E501

        Last modification time of order (in milliseconds)  # noqa: E501

        :return: The update_time_ms of this Order.  # noqa: E501
        :rtype: int
        """
        return self._update_time_ms

    @update_time_ms.setter
    def update_time_ms(self, update_time_ms):
        """Sets the update_time_ms of this Order.

        Last modification time of order (in milliseconds)  # noqa: E501

        :param update_time_ms: The update_time_ms of this Order.  # noqa: E501
        :type: int
        """

        self._update_time_ms = update_time_ms

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501

        Order status  - `open`: to be filled - `closed`: filled - `cancelled`: cancelled  # noqa: E501

        :return: The status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.

        Order status  - `open`: to be filled - `closed`: filled - `cancelled`: cancelled  # noqa: E501

        :param status: The status of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "closed", "cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(status, allowed_values)  # noqa: E501
            )

        self._status = status

    @property
    def currency_pair(self):
        """Gets the currency_pair of this Order.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The currency_pair of this Order.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this Order.

        Currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this Order.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_pair is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_pair`, must not be `None`")  # noqa: E501

        self._currency_pair = currency_pair

    @property
    def type(self):
        """Gets the type of this Order.  # noqa: E501

        Order Type   - limit : Limit Order - market : Market Order  # noqa: E501

        :return: The type of this Order.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Order.

        Order Type   - limit : Limit Order - market : Market Order  # noqa: E501

        :param type: The type of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["limit", "market"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values)  # noqa: E501
            )

        self._type = type

    @property
    def account(self):
        """Gets the account of this Order.  # noqa: E501

        Account type. spot - use spot account; margin - use margin account; cross_margin - use cross margin account. Portfolio margin account must set to `cross-margin`   # noqa: E501

        :return: The account of this Order.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Order.

        Account type. spot - use spot account; margin - use margin account; cross_margin - use cross margin account. Portfolio margin account must set to `cross-margin`   # noqa: E501

        :param account: The account of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["spot", "margin", "cross_margin"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and account not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `account` ({0}), must be one of {1}".format(account, allowed_values)  # noqa: E501
            )

        self._account = account

    @property
    def side(self):
        """Gets the side of this Order.  # noqa: E501

        Order side  # noqa: E501

        :return: The side of this Order.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Order.

        Order side  # noqa: E501

        :param side: The side of this Order.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        allowed_values = ["buy", "sell"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and side not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}".format(side, allowed_values)  # noqa: E501
            )

        self._side = side

    @property
    def amount(self):
        """Gets the amount of this Order.  # noqa: E501

        When `type` is limit, it refers to base currency.  For instance, `BTC_USDT` means `BTC`  When `type` is `market`, it refers to different currency according to `side`  - `side` : `buy` means quote currency, `BTC_USDT` means `USDT` - `side` : `sell` means base currency，`BTC_USDT` means `BTC`   # noqa: E501

        :return: The amount of this Order.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Order.

        When `type` is limit, it refers to base currency.  For instance, `BTC_USDT` means `BTC`  When `type` is `market`, it refers to different currency according to `side`  - `side` : `buy` means quote currency, `BTC_USDT` means `USDT` - `side` : `sell` means base currency，`BTC_USDT` means `BTC`   # noqa: E501

        :param amount: The amount of this Order.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this Order.  # noqa: E501

        Price can't be empty when `type`= `limit`  # noqa: E501

        :return: The price of this Order.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Order.

        Price can't be empty when `type`= `limit`  # noqa: E501

        :param price: The price of this Order.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def time_in_force(self):
        """Gets the time_in_force of this Order.  # noqa: E501

        Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee - fok: FillOrKill, fill either completely or none Only `ioc` and `fok` are supported when `type`=`market`  # noqa: E501

        :return: The time_in_force of this Order.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this Order.

        Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee - fok: FillOrKill, fill either completely or none Only `ioc` and `fok` are supported when `type`=`market`  # noqa: E501

        :param time_in_force: The time_in_force of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["gtc", "ioc", "poc", "fok"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and time_in_force not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `time_in_force` ({0}), must be one of {1}".format(  # noqa: E501
                    time_in_force, allowed_values
                )
            )

        self._time_in_force = time_in_force

    @property
    def iceberg(self):
        """Gets the iceberg of this Order.  # noqa: E501

        Amount to display for the iceberg order. Null or 0 for normal orders. Set to -1 to hide the order completely  # noqa: E501

        :return: The iceberg of this Order.  # noqa: E501
        :rtype: str
        """
        return self._iceberg

    @iceberg.setter
    def iceberg(self, iceberg):
        """Sets the iceberg of this Order.

        Amount to display for the iceberg order. Null or 0 for normal orders. Set to -1 to hide the order completely  # noqa: E501

        :param iceberg: The iceberg of this Order.  # noqa: E501
        :type: str
        """

        self._iceberg = iceberg

    @property
    def auto_borrow(self):
        """Gets the auto_borrow of this Order.  # noqa: E501

        Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough.  # noqa: E501

        :return: The auto_borrow of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._auto_borrow

    @auto_borrow.setter
    def auto_borrow(self, auto_borrow):
        """Sets the auto_borrow of this Order.

        Used in margin or cross margin trading to allow automatic loan of insufficient amount if balance is not enough.  # noqa: E501

        :param auto_borrow: The auto_borrow of this Order.  # noqa: E501
        :type: bool
        """

        self._auto_borrow = auto_borrow

    @property
    def auto_repay(self):
        """Gets the auto_repay of this Order.  # noqa: E501

        Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  1. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders. 2. `auto_borrow` and `auto_repay` cannot be both set to true in one order.  # noqa: E501

        :return: The auto_repay of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._auto_repay

    @auto_repay.setter
    def auto_repay(self, auto_repay):
        """Sets the auto_repay of this Order.

        Enable or disable automatic repayment for automatic borrow loan generated by cross margin order. Default is disabled. Note that:  1. This field is only effective for cross margin orders. Margin account does not support setting auto repayment for orders. 2. `auto_borrow` and `auto_repay` cannot be both set to true in one order.  # noqa: E501

        :param auto_repay: The auto_repay of this Order.  # noqa: E501
        :type: bool
        """

        self._auto_repay = auto_repay

    @property
    def left(self):
        """Gets the left of this Order.  # noqa: E501

        Amount left to fill  # noqa: E501

        :return: The left of this Order.  # noqa: E501
        :rtype: str
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this Order.

        Amount left to fill  # noqa: E501

        :param left: The left of this Order.  # noqa: E501
        :type: str
        """

        self._left = left

    @property
    def fill_price(self):
        """Gets the fill_price of this Order.  # noqa: E501

        Total filled in quote currency. Deprecated in favor of `filled_total`  # noqa: E501

        :return: The fill_price of this Order.  # noqa: E501
        :rtype: str
        """
        return self._fill_price

    @fill_price.setter
    def fill_price(self, fill_price):
        """Sets the fill_price of this Order.

        Total filled in quote currency. Deprecated in favor of `filled_total`  # noqa: E501

        :param fill_price: The fill_price of this Order.  # noqa: E501
        :type: str
        """

        self._fill_price = fill_price

    @property
    def filled_total(self):
        """Gets the filled_total of this Order.  # noqa: E501

        Total filled in quote currency  # noqa: E501

        :return: The filled_total of this Order.  # noqa: E501
        :rtype: str
        """
        return self._filled_total

    @filled_total.setter
    def filled_total(self, filled_total):
        """Sets the filled_total of this Order.

        Total filled in quote currency  # noqa: E501

        :param filled_total: The filled_total of this Order.  # noqa: E501
        :type: str
        """

        self._filled_total = filled_total

    @property
    def fee(self):
        """Gets the fee of this Order.  # noqa: E501

        Fee deducted  # noqa: E501

        :return: The fee of this Order.  # noqa: E501
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this Order.

        Fee deducted  # noqa: E501

        :param fee: The fee of this Order.  # noqa: E501
        :type: str
        """

        self._fee = fee

    @property
    def fee_currency(self):
        """Gets the fee_currency of this Order.  # noqa: E501

        Fee currency unit  # noqa: E501

        :return: The fee_currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._fee_currency

    @fee_currency.setter
    def fee_currency(self, fee_currency):
        """Sets the fee_currency of this Order.

        Fee currency unit  # noqa: E501

        :param fee_currency: The fee_currency of this Order.  # noqa: E501
        :type: str
        """

        self._fee_currency = fee_currency

    @property
    def point_fee(self):
        """Gets the point_fee of this Order.  # noqa: E501

        Points used to deduct fee  # noqa: E501

        :return: The point_fee of this Order.  # noqa: E501
        :rtype: str
        """
        return self._point_fee

    @point_fee.setter
    def point_fee(self, point_fee):
        """Sets the point_fee of this Order.

        Points used to deduct fee  # noqa: E501

        :param point_fee: The point_fee of this Order.  # noqa: E501
        :type: str
        """

        self._point_fee = point_fee

    @property
    def gt_fee(self):
        """Gets the gt_fee of this Order.  # noqa: E501

        GT used to deduct fee  # noqa: E501

        :return: The gt_fee of this Order.  # noqa: E501
        :rtype: str
        """
        return self._gt_fee

    @gt_fee.setter
    def gt_fee(self, gt_fee):
        """Sets the gt_fee of this Order.

        GT used to deduct fee  # noqa: E501

        :param gt_fee: The gt_fee of this Order.  # noqa: E501
        :type: str
        """

        self._gt_fee = gt_fee

    @property
    def gt_maker_fee(self):
        """Gets the gt_maker_fee of this Order.  # noqa: E501

        GT used to deduct maker fee  # noqa: E501

        :return: The gt_maker_fee of this Order.  # noqa: E501
        :rtype: str
        """
        return self._gt_maker_fee

    @gt_maker_fee.setter
    def gt_maker_fee(self, gt_maker_fee):
        """Sets the gt_maker_fee of this Order.

        GT used to deduct maker fee  # noqa: E501

        :param gt_maker_fee: The gt_maker_fee of this Order.  # noqa: E501
        :type: str
        """

        self._gt_maker_fee = gt_maker_fee

    @property
    def gt_taker_fee(self):
        """Gets the gt_taker_fee of this Order.  # noqa: E501

        GT used to deduct taker fee  # noqa: E501

        :return: The gt_taker_fee of this Order.  # noqa: E501
        :rtype: str
        """
        return self._gt_taker_fee

    @gt_taker_fee.setter
    def gt_taker_fee(self, gt_taker_fee):
        """Sets the gt_taker_fee of this Order.

        GT used to deduct taker fee  # noqa: E501

        :param gt_taker_fee: The gt_taker_fee of this Order.  # noqa: E501
        :type: str
        """

        self._gt_taker_fee = gt_taker_fee

    @property
    def gt_discount(self):
        """Gets the gt_discount of this Order.  # noqa: E501

        Whether GT fee discount is used  # noqa: E501

        :return: The gt_discount of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._gt_discount

    @gt_discount.setter
    def gt_discount(self, gt_discount):
        """Sets the gt_discount of this Order.

        Whether GT fee discount is used  # noqa: E501

        :param gt_discount: The gt_discount of this Order.  # noqa: E501
        :type: bool
        """

        self._gt_discount = gt_discount

    @property
    def rebated_fee(self):
        """Gets the rebated_fee of this Order.  # noqa: E501

        Rebated fee  # noqa: E501

        :return: The rebated_fee of this Order.  # noqa: E501
        :rtype: str
        """
        return self._rebated_fee

    @rebated_fee.setter
    def rebated_fee(self, rebated_fee):
        """Sets the rebated_fee of this Order.

        Rebated fee  # noqa: E501

        :param rebated_fee: The rebated_fee of this Order.  # noqa: E501
        :type: str
        """

        self._rebated_fee = rebated_fee

    @property
    def rebated_fee_currency(self):
        """Gets the rebated_fee_currency of this Order.  # noqa: E501

        Rebated fee currency unit  # noqa: E501

        :return: The rebated_fee_currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._rebated_fee_currency

    @rebated_fee_currency.setter
    def rebated_fee_currency(self, rebated_fee_currency):
        """Sets the rebated_fee_currency of this Order.

        Rebated fee currency unit  # noqa: E501

        :param rebated_fee_currency: The rebated_fee_currency of this Order.  # noqa: E501
        :type: str
        """

        self._rebated_fee_currency = rebated_fee_currency

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
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()
