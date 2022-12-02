import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import Sequence

from .strategy import Strategy
from .symbol import Symbol
from .config import Config


class Executor:
    """
    Executor class for running multiple strategies and instruments concurrently.

    Attributes:
        executor (ThreadPoolExecutor, ProcessPoolExecutor): Executor object.
        workers (list): List of strategies.

    """
    def __init__(self):
        self.config = Config()
        self.executor = ThreadPoolExecutor if self.config.executor == 'thread' else ProcessPoolExecutor
        self.workers: list[type(Strategy)] = []

    def add_workers(self, strategies: Sequence[type(Strategy)]):
        """
        Add multiple strategies at once

        Args:
            strategies (Sequence[Strategy]): A sequence of strategies.

        Returns:
        """
        self.workers.extend(strategies)

    def remove_workers(self, *symbols: Sequence[Symbol]):
        """
        Remove worker if the symbol of the strategy did not initialize successfully
        Returns:
        """
        for strategy in self.workers:
            if strategy.symbol not in symbols:
                self.workers.remove(strategy)

    def add_worker(self, strategy: type(Strategy)):
        """
        Add a strategy object to the list of workers
        Args:
            strategy (Strategy): A strategy object

        Returns:

        """
        self.workers.append(strategy)

    @staticmethod
    def run(strategy: type(Strategy)):
        """
        Wrap the coroutine in asyncio.run for each thread.
        Args:
            strategy (Strategy): A strategy object

        Returns:

        """
        asyncio.run(strategy.trade())

    def execute(self, workers: int = 0):
        """
        Add workers to pool executors.

        Args:
            workers: Number of workers to use in executor pool. Defaults to zero

        Returns:

        """
        workers = workers or len(self.workers)
        with self.executor(max_workers=workers) as executor:
            executor.map(self.run, self.workers)
