import asyncio
from time import time
from typing import List, Optional

from rich.console import (
    Console,
    ConsoleOptions,
    ConsoleRenderable,
    Control,
    RenderResult,
)
from rich.control import ControlType
from rich.live import Live
from rich.spinner import Spinner

from .node import Node
from .request import Request, RequestState


MAX_NODE_ITER = 10


class StatusBar(ConsoleRenderable):  # type: ignore
    def __init__(self, ready_nodes: List[Node], in_progress_display: bool = True):
        self.in_progress_display = in_progress_display
        self.start_time = time()
        self.requests_status = {"success": 0, "error": 0, "completed": 0}
        self.spinner: Spinner = Spinner(name="dots")
        self._ready_nodes = ready_nodes
        self._in_progress_node: Optional[Node] = None

    def notify_request(self, request: Request) -> None:
        if request.state is RequestState.COMPLETED:
            self.requests_status["completed"] += 1
            if request.ok():
                self.requests_status["success"] += 1
            else:
                self.requests_status["error"] += 1

    def notify_finalized_node(self, node: Node) -> None:
        if node is self._in_progress_node:
            self._in_progress_node = None

    def elapsed_time(self) -> float:
        return time() - self.start_time

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:

        if self.in_progress_display:
            if not self._in_progress_node:
                max_count_in_progress = 0
                for i, node in enumerate(self._ready_nodes):
                    node_count_in_progress = node.count_in_progress()
                    if node_count_in_progress > max_count_in_progress:
                        self._in_progress_node = node
                        max_count_in_progress = node_count_in_progress
                    if self._in_progress_node and i > MAX_NODE_ITER:
                        break

            if self._in_progress_node:
                self.spinner.text = self._in_progress_node.get_result_string()
            else:
                self.spinner.text = "pending requests..."
            yield self.spinner

        yield (
            f"Completed: {self.requests_status['completed']} "
            f"| Success: {self.requests_status['success']} "
            f"| Error: {self.requests_status['error']} "
            f"| Elapsed time: {self.elapsed_time():.1f}s "
        )


class Output:
    def __init__(
        self,
        # in_progress_display: int = 3,
        # status_bar: bool = True,
    ):
        self.console = Console()
        self._ready_nodes: List[Node] = []
        self._finalized_nodes: List[Node] = []
        self._status_bar = StatusBar(self._ready_nodes)

    async def start(self):
        try:
            self.console.show_cursor(False)
            with Live(
                console=self.console,
                renderable=self._status_bar,
                auto_refresh=False,
                transient=True,
            ) as live:
                while True:
                    self.process_ready_nodes()
                    self.display_finalized_nodes()
                    live.refresh()
                    await asyncio.sleep(0.05)

        except asyncio.CancelledError:
            raise

        finally:
            self.process_ready_nodes()
            self.display_finalized_nodes()
            self.console.show_cursor(True)

    def display_finalized_nodes(self):
        for node in self._finalized_nodes:
            self.console.print(
                node.get_result_string(),
                end=f"{Control((ControlType.ERASE_IN_LINE, 0))}\n",
            )
        self._finalized_nodes = []

    def process_ready_nodes(self) -> None:
        finalized_nodes = []
        ready_nodes_gen = (
            self._ready_nodes[i]
            for i in range(min(MAX_NODE_ITER, len(self._ready_nodes)))
        )
        for node in ready_nodes_gen:
            if node.links_all_completed():
                self._finalized_nodes.append(node)
                self._status_bar.notify_finalized_node(node)
                finalized_nodes.append(node)
        for node in finalized_nodes:
            self._ready_nodes.remove(node)

    def notify_node(self, node: Node) -> None:
        self._ready_nodes.append(node)

    def notify_request(self, request: Request) -> None:
        self._status_bar.notify_request(request)
