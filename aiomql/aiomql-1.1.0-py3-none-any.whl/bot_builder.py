import asyncio
from typing import Sequence, Type
import logging

from .core.meta_trader import MetaTrader
from .executor import Executor
from .account import account, Account
from .market import Market
from .symbol import Symbol
from .strategy import Strategy
from .config import Config

logger = logging.getLogger()


class Bot:
    """
    Bot builder class

    Args:
        market (Market): Financial Market containing the instruments you wish to trade on

    Keyword Args:
        market (Market): Financial Market containing the instruments you wish to trade on
        mt5: MetaTrade class
        account (Account): Account object

    Attributes:
        account (Account): Account Object
        executor: Bot Executor
        market (Market): Financial Market containing the instruments you wish to trade on
        mt5: MetaTrade class
        config: Config Object
        remove_bad_symbols (bool): If true remove symbols that were not successfully initialized

    """
    def __init__(self, *, market: Market = Market(), mt5=MetaTrader(), account: Account = account, remove_bad_symbols: bool = True):
        self.config = Config()
        self.account = account
        self.account.set_attributes(account_number=self.config.account_number, password=self.config.password, server=self.config.server)
        self.executor = Executor()
        self.market = market
        self.mt5 = mt5
        self.remove_bad_symbols = remove_bad_symbols

    def create_records_dir(self):
        self.config.records_dir.mkdir(parents=True, exist_ok=True)

    async def initialize(self):
        init = await self.mt5.initialize(login=self.account.account_number, server=account.server, password=account.password)
        if not init:
            logger.error("Unable to initialize terminal")
            exit(0)
        logger.info("Initialized Terminal")

        connect = await self.account.login()
        if not connect:
            logger.error("Unable to login into to account terminal")
            exit(0)
        logger.info("Login Successful")

        await self.market.init_symbols()

    def execute(self):
        asyncio.run(self.initialize())

        if self.config.record_trades:
            self.create_records_dir()

        print("Starting the Bot")
        if self.remove_bad_symbols:
            self.executor.remove_workers(*self.market.symbols)
        self.executor.execute()

    def add_single(self, *, strategy: Strategy):
        """
        Add a single standalone strategy without any market object
        Args:
            strategy (Strategy): Strategy

        Returns:
        """
        self.market.add(symbol=strategy.symbol)
        self.executor.add_worker(strategy)

    def add_strategy(self, strategy: type(Strategy)):
        """
        Add a strategy to the executor
        Args:
            strategy: Strategy to run on bot

        Returns:

        Notes: Make sure the symbol has been added to the market

        """
        self.executor.add_worker(strategy)

    def add_strategies(self, strategies: list[type(Strategy)]):
        """
        Add multiple strategies at the same time

        Args:
            strategies: A list of strategies

        Returns:

        """
        self.executor.add_workers(strategies)

    def add_strategy_all(self, *, strategy: Type[Strategy], params: dict | None = None):
        """
        Use this to run a strategy on all available instruments in the market using the default parameters a one parameters for all symbols

        Keyword Args:
            strategy: Strategy class

            params: A dictionary of parameters for the strategy

        Returns:

        """
        self.market.select_all()
        [self.add_strategy(strategy(symbol=symbol, params=params)) for symbol in self.market.symbols]

    def add_strategy_many(self, *, strategy: Type[Strategy], symbols: Sequence[str], params: dict | None = None):
        """
        Multiple strategies at once

        Keyword Args:
            strategy:
            symbols:
            params:

        Returns:
        """
        symbols = self.market.select(*symbols)
        [self.add_strategy(strategy(symbol=symbol, params=params)) for symbol in symbols]
