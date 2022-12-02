import asyncio
from datetime import datetime

from .config import Config

from .core.meta_trader import MetaTrader
from .core.models import TradeDeal, TradeOrder
from .terminal import terminal


class History:
    """
    The history class handles trade deals and trade orders in the trading history.

    Args:
        mt5 (MetaTrader): The Meta trader object for connecting to the terminal. Default Keyword Argument.


        date_from (datetime, float): Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since
            1970.01.01. Defaults to the current time in "utc"


        date_to (datetime, float): Date, up to which the orders are requested. Set by the 'datetime' object or as a number of
            seconds elapsed since 1970.01.01. Defaults to the current time in "utc"


        group (str): Filter for selecting history by symbols.


        ticket (int): Filter for selecting history by ticket number


        position (int): Filter for selecting history deals by position

    Attributes:
        deals (Iterable[TradeDeal]): Iterable of trade deals
        orders (Iterable[TradeOrder]): Iterable of trade orders
        total_deals: Total number of deals
        total_orders (int): Total number orders
        group (str): Filter for selecting history by symbols.
        ticket (int): Filter for selecting history by ticket number
        position (int): Filter for selecting history deals by position
        initialized (bool): check if initial request has been sent to the terminal to get history.
    """
    deals: list[TradeDeal] = []
    orders: list[TradeOrder] = []
    total_deals: int = 0
    total_orders: int = 0

    def __init__(self, *, mt5=MetaTrader(), date_from: datetime | float = datetime.utcnow(), date_to: datetime | float = datetime.utcnow(),
                 group: str = "", ticket: int = 0, position: int = 0):
        self.config = Config()
        self.mt5 = mt5
        self.date_from = date_from
        self.date_to = date_to
        self.group = group
        self.ticket = ticket
        self.position = position
        self.initialized = False

    async def init(self, deals=True, orders=True) -> bool:
        """
        Get history deals and orders
        Keyword Args:
            deals (bool): If true get history deals during initial request to terminal
            orders (bool): If true get history orders during initial request to terminal

        Returns:
            bool: True if all requests were successful else False

        """
        tasks = []
        tasks.append(self.get_deals()) if deals else ...
        tasks.append(self.get_orders()) if orders else ...
        res = await asyncio.gather(*tasks)
        self.initialized = all(res)
        return self.initialized

    async def get_deals(self) -> list[TradeDeal]:
        """
        Get trade deals
        Returns:
            list[TradeDeal]: Iterable of trade deals

        """
        deals = await self.mt5.history_deals_get(date_from=self.date_from, date_to=self.date_to, group=self.group, ticket=self.ticket,
                                                 position=self.position)

        self.deals = [TradeDeal(**deal._asdict()) for deal in deals] if deals else []
        self.total_deals = len(self.deals)
        return self.deals

    async def deals_total(self) -> int:
        """
        Get total number of deals
        Returns (int): Number of Deals
        """
        self.total_deals = await self.mt5.history_deals_total(self.date_from, self.date_to)
        return self.total_deals

    async def get_orders(self) -> list[TradeOrder]:
        """
        Get trade orders
        Returns:
            list[TradeOrder]): Iterable of trade orders
        """

        orders = await self.mt5.history_orders_get(date_from=self.date_from, date_to=self.date_to, group=self.group, ticket=self.ticket,
                                                   position=self.position)
        self.orders = [TradeOrder(**order._asdict()) for order in orders] if orders else []
        self.total_orders = len(self.orders)
        return self.orders

    async def orders_total(self) -> int:
        """
        Get total number of orders
        Returns (int): Number of orders
        """
        self.total_orders = await self.mt5.history_orders_total(self.date_from, self.date_to)
        return self.total_orders
