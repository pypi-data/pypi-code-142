from __future__ import annotations

import logging
from contextvars import copy_context
from dataclasses import dataclass
from functools import partial
from os import PathLike
from typing import IO, Iterator, Optional

from tqdm import tqdm  # type: ignore
from typeguard import check_type

from .supplychain import SupplyChain
from .types import ControlStrategy, ReleaseStrategy
from .utils import context
from .utils.context import iter_nodes
from .utils.metrics import MetricsExporter, setup_metrics


@dataclass
class Simulator:
    """SupplyChain Simulator

    Simulate a supply-chain using the provided control and release strategy

    Arguments:
        supply_chain: the supply-chain to simulate
        control_strategy: Determines how orders are created during the simulation
            should adhere to the ControlStrategy Protocol
        release_strategy: Determines how orders are released from each Node during simulation
            should adhere to the ReleaseStrategy Protocol
        filename: File to write the metrics too
            outputs results to the current workingdirectory by default
        stream: Optional additional metrics stream to add.
        max_bytes: Maximum size of the output file
            A new file will be opened when max_bytes will be exceeded.
            default (0) will never create a new file
        level: The log level
            Options are logging.INFO and logging.DEBUG
    Raises:
        ValueError: if the strategies don't implement the correct Protocol
    """

    supply_chain: SupplyChain
    control_strategy: ControlStrategy
    release_strategy: ReleaseStrategy
    filename: str | PathLike[str] | None = None
    max_bytes: int = 0
    stream: Optional[IO[str]] = None
    level: int = logging.INFO

    def __post_init__(self) -> None:
        """Check if the provided strategies implement the correct interface"""
        check_type("control_strategy", self.control_strategy, ControlStrategy)
        check_type("release_strategy", self.release_strategy, ReleaseStrategy)
        self._metrics: MetricsExporter | None = None

    @property
    def output(self) -> Iterator[PathLike[str]]:
        """Return the filename(s) of the metrics FileHandler"""
        if self._metrics:
            yield from self._metrics.output

    def run(
        self,
        periods: int,
        /,
        loops: int = 1,
    ) -> None:
        """Run the simulation for a number of periods

        Arguments:
            periods: number of periods to simulate
            loops: number of times the simulation from start to end period is run.
            The stock, orders, and pipeline are carried over from one loop to the next.
        """
        ctx = copy_context()
        ctx.run(partial(self._run, periods, loops=loops))

    def _run(
        self,
        periods: int,
        /,
        loops: int,
    ) -> None:
        """Run the simulation"""

        # Check if all nodes have their llc set
        for node in self.supply_chain.nodes.values():
            if not isinstance(node.llc, int) or node.llc < 0:
                raise ValueError(f"{node} has an invalid llc: {node.llc}")

        self._metrics = setup_metrics(
            filename=self.filename,
            level=self.level,
            stream=self.stream,
            max_bytes=self.max_bytes,
        )
        status = tqdm(total=loops * periods)
        try:
            for loop in range(0, loops):
                context.loop.set(loop)
                for period_loop in range(1, periods + 1):
                    period = loop * periods + period_loop
                    context.period.set(period)
                    self.simulate_period(period=period)
                    status.update(1)
                    for node in self.supply_chain.nodes.values():
                        node.log_state()
                self.reuse_data(periods)
        finally:
            self._metrics.stop_metrics()
            status.close()

    def simulate_period(self, period: int) -> None:
        """Simulate a single period"""
        # accept receipts
        for node in iter_nodes(self.supply_chain.nodes.values()):
            node.satisfy_received_receipts()

        # assemble / produce
        for node in iter_nodes(self.supply_chain.nodes.values()):
            node.assemble()

        # satisfy backorders
        for node in iter_nodes(self.supply_chain.nodes.values()):
            node.satisfy_backorders()

        # satisfy sales
        for node in iter_nodes(self.supply_chain.nodes.values()):
            node.satisfy_sales(period=period)

        # move pipeline
        for node in iter_nodes(self.supply_chain.nodes.values()):
            node.pipeline.update_pipeline()

        # starting at the end nodes, moving upstream
        for llc in range(self.supply_chain.max_llc + 1):
            for node in iter_nodes(self.supply_chain.nodes_by_llc(llc)):
                # determine order size
                orders = self.control_strategy.get_orders(node=node, period=period)
                # create new orders
                self.supply_chain._create_orders(  # pylint: disable=protected-access
                    node=node, orders=orders, period=period
                )
                # create order release
                order_releases = self.release_strategy.get_releases(node)
                # release orders
                self.supply_chain._release_orders(  # pylint: disable=protected-access
                    node=node, releases=order_releases, period=period
                )

    def reuse_data(self, loop_size: int):
        """Shift input data index based on the total number of loops"""
        for node in iter_nodes(self.supply_chain.nodes.values()):
            node.loop_data(loop_size=loop_size)
            self.control_strategy.loop_data(node=node, loop_size=loop_size)
