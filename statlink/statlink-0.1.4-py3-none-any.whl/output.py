import asyncio
from time import time
from typing import Dict, List, Optional

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


class StatusBar(ConsoleRenderable):  # type: ignore
    def __init__(self, in_progress_display: bool = True):
        self.in_progress_display = in_progress_display
        self.start_time = time()
        self.requests_status = {"queued": 0, "success": 0, "error": 0, "completed": 0}
        self.spinner: Spinner = Spinner(name="dots")
        self.completed_nodes: Dict[str, Node] = {}
        self.in_progress_node: Optional[Node] = None

    def notify_request(self, request: Request) -> None:
        if request.state is RequestState.COMPLETED:
            self.requests_status["completed"] += 1
            if request.ok():
                self.requests_status["success"] += 1
            else:
                self.requests_status["error"] += 1

    def notify_node(self, node: Node, children_completed: bool = False) -> None:
        if node.location in self.completed_nodes:
            if children_completed:
                del self.completed_nodes[node.location]
                if node is self.in_progress_node:
                    self.in_progress_node = None
        else:
            self.completed_nodes[node.location] = node

    def elapsed_time(self) -> float:
        return time() - self.start_time

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:

        if self.in_progress_display:
            if not self.in_progress_node:
                in_progress_nodes: List[Node] = sorted(
                    [
                        node
                        for node in self.completed_nodes.values()
                        if node.count_in_progress() > 0
                    ],
                    key=lambda node: node.count_in_progress(),
                    reverse=True,
                )
                self.in_progress_node = next(iter(in_progress_nodes), None)

            if self.in_progress_node:
                self.spinner.text = self.in_progress_node.get_result_string()
            else:
                self.spinner.text = "pending requests..."
            yield self.spinner

        yield (
            f"Completed: {self.requests_status['completed']} "
            f"| Success: {self.requests_status['success']} "
            f"| Error: {self.requests_status['error']} "
            f"| Elapsed time: {self.elapsed_time():.1f}s"
        )


class Output:
    def __init__(
        self,
        # in_progress_display: int = 3,
        # status_bar: bool = True,
    ):
        self.console = Console()
        self._ready_nodes = {}
        self._completed_requests = {}
        self._status_bar = StatusBar()

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
                    self.display_completed_nodes()
                    live.refresh()
                    await asyncio.sleep(0.05)

        except asyncio.CancelledError:
            raise

        finally:
            self.display_completed_nodes()
            self.console.show_cursor(True)

    def display_completed_nodes(self) -> None:
        displayed_locations = []
        for location, node in self._ready_nodes.items():
            if node.links_all_completed():
                self.console.print(
                    node.get_result_string(),
                    end=f"{Control((ControlType.ERASE_IN_LINE, 0))}\n",
                )
                self._status_bar.notify_node(node, children_completed=True)
                displayed_locations.append(location)
        for location in displayed_locations:
            del self._ready_nodes[location]

    def notify_node(self, node: Node) -> None:
        self._ready_nodes[node.location] = node
        self._status_bar.notify_node(node)

    def notify_request(self, request: Request) -> None:
        self._status_bar.notify_request(request)
