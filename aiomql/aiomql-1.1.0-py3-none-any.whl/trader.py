from abc import ABC, abstractmethod

from .account import Account, account
from .order import Order
from .result import TradeResult
from .symbol import Symbol


class Trader(ABC):
    """
    Helper class for creating a Trader object. Handles the initializing of an order and the placing of trades
    Args:
        symbol (Symbol): Financial instrument

        account (Account): Trading account

    Attributes:

        symbol (Symbol): Financial instrument class Symbol class or a subclass of it.

        account (Account): Trading account

        order (Order): Trade order
    """
    def __init__(self, *, symbol: type(Symbol), account: Account = account):
        self.account = account
        self.symbol = symbol
        self.order = Order(symbol=symbol.name)

    async def create_order(self, *args, **kwargs):
        """
        Create an order, and update the order object initialized
        Args:
            *args:
            **kwargs:

        Returns:

        """

    @abstractmethod
    async def place_trade(self, *args, **kwargs) -> TradeResult | None:
        """
        Send trade to server
        Args:
            *args:
            **kwargs:

        Returns: TradeResult if successful

        """
