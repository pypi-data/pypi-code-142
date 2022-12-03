import asyncio
from contextlib import asynccontextmanager
from dataclasses import dataclass
from signal import SIGINT, SIGTERM
from typing import Any, AsyncGenerator, Iterable, List, Optional, Set, Type, Union

from aiolimiter import AsyncLimiter

from .engine import ENGINE_MAPPING, Engine
from .filter import DomainFilter, OrFilter
from .node import Node
from .output import Output
from .request import Request, RequestState
from .source import FileSource, GenericSource, HTMLSource
from .store import Store
from .utils import get_files_path, is_url


DEFAULT_CONCURRENCY = 20
DEFAULT_RECURSION_MODE = "internal"
DEFAULT_CHECK_MODE = "all"
DEFAULT_DEPTH = -1
DEFAULT_TIMEOUT = 20
DEFAULT_ENGINE = "aiohttp"
DEFAULT_MAX_RETRY = 1
DEFAULT_MIN_QUEUE_SIZE = 1000
DEFAULT_RATE_LIMIT = 20


@dataclass
class CrawlerResult:
    requests: List[Request]
    nodes: List[Node]


class Crawler:
    def __init__(
        self,
        concurrency: int = DEFAULT_CONCURRENCY,
        recursion_mode: str = DEFAULT_RECURSION_MODE,
        check_mode: str = DEFAULT_CHECK_MODE,
        depth: int = DEFAULT_DEPTH,
        timeout: int = DEFAULT_TIMEOUT,
        max_retry: int = DEFAULT_MAX_RETRY,
        engine: Union[str, Type[Engine]] = DEFAULT_ENGINE,
        min_queue_size: int = DEFAULT_MIN_QUEUE_SIZE,
        rate_limit: int = DEFAULT_RATE_LIMIT,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        self.loop = loop or asyncio.get_event_loop()
        self.concurrency = concurrency
        self.depth = depth
        self.timeout = timeout
        self.max_retry = max_retry
        self.recursion_mode = recursion_mode
        self.recursion_filter = OrFilter([])
        self.check_mode = check_mode
        self.check_filter = OrFilter([])
        self.store = Store()
        self.output = Output()
        self.requests_queue: asyncio.Queue[Request] = asyncio.Queue()
        self.sources_queue: asyncio.Queue[GenericSource] = asyncio.Queue()
        self.tasks: Set[asyncio.Task[Any]] = set()
        self.min_queue_size = min_queue_size
        self._stopping: bool = False
        self._limiter = AsyncLimiter(max_rate=rate_limit, time_period=1)

        if isinstance(engine, type) and issubclass(engine, Engine):
            self.engine_class = engine
        elif isinstance(engine, str):
            self.engine_class = ENGINE_MAPPING.get(engine)  # type: ignore

        if self.engine_class is None:
            raise Exception(f"Cannot instanciate Crawler with engine: {engine}")

    def start(self, sources: Iterable[str]) -> CrawlerResult:
        for signal in (SIGINT, SIGTERM):
            self.loop.add_signal_handler(
                signal, lambda: asyncio.create_task(self.stop())
            )

        try:
            self.loop.run_until_complete(self._async_start(sources))
        finally:
            self.display_result()

        return CrawlerResult(
            requests=self.store.get_requests_completed(),
            nodes=self.store.get_nodes_processed(),
        )

    async def _async_start(self, sources: Iterable[str]) -> None:

        # Initialize startup sources
        for source in sources:
            if is_url(source):
                if self.recursion_mode == "internal":
                    self.recursion_filter.append(DomainFilter.from_url(source))
                if self.check_mode == "internal":
                    self.check_filter.append(DomainFilter.from_url(source))
                self.add_request(url=source)
            else:
                for file_path in get_files_path(source):
                    file_source = FileSource.from_path(file_path)
                    await self.add_source(file_source)

        # Initialize workers
        async with self.engine_class() as engine:
            request_workers = [
                self._request_worker(engine) for _ in range(self.concurrency)
            ]
            self.tasks = {
                asyncio.create_task(coro)
                for coro in [
                    *request_workers,
                    self.source_worker(),
                    self.output.start(),
                    self.requests_queue.join(),
                ]
            }
            # Here we wait for the requests manager to have no more requests
            # to process and for other tasks to capture inner tasks
            # exceptions different from asyncio.CancelledError
            while not (self.requests_queue.empty() and self.sources_queue.empty()):
                done, pending = await asyncio.wait(
                    self.tasks, return_when=asyncio.FIRST_COMPLETED
                )
                if any(task.cancelled() for task in done):
                    break

            for task in done:
                if not task.cancelled():
                    exc = task.exception()
                    if exc:
                        raise exc
            if not self._stopping:
                await self.stop(tasks=pending)

    async def stop(
        self, tasks: Optional[Set[asyncio.Task]] = None  # type: ignore
    ) -> None:
        self._stopping = True
        tasks = tasks or self.tasks
        if tasks:
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)

    async def add_source(self, source: GenericSource) -> None:
        source_node = self.store.create_or_get_node(location=source.location)
        for url in await source.find_urls():
            if self.check_filter.validate(url):
                self.add_request(url=url, depth=source.depth)
                self.store.add_edge(source_node.location, url)
        self.output.notify_node(source_node)

    def add_request(
        self,
        url: str,
        depth: int = 0,
    ) -> None:
        request = self.store.get_request(url=url)
        if not request:
            request = Request(
                url=url, depth=depth, timeout=self.timeout, max_retry=self.max_retry
            )
            self.store.add_request(request)
            self.requests_queue.put_nowait(request)
            self.output.notify_request(request)

    @asynccontextmanager
    async def _request_context(self, request: Request) -> AsyncGenerator[None, None]:
        async with self._limiter:
            self._set_request_state(request, RequestState.IN_PROGRESS)
            yield
            self._set_request_state(request, RequestState.COMPLETED)

    def _set_request_state(self, request: Request, request_state: RequestState) -> None:
        request.state = request_state
        self.output.notify_request(request)

    async def _request_worker(self, engine: Engine) -> None:
        while True:
            request = await self.requests_queue.get()
            async with self._request_context(request):
                response = await request.fetch(engine)
            if (
                self.recursion_filter.validate(request.url)
                and response
                and response.text
                and response.ok()
                and (self.depth < 0 or request.depth < self.depth)
            ):
                source = HTMLSource(
                    content=response.text, location=request.url, depth=request.depth + 1
                )

                if (
                    self.requests_queue.qsize() < self.min_queue_size
                    and self.sources_queue.empty()
                ):
                    await self.add_source(source)
                else:
                    self.sources_queue.put_nowait(source)

            self.requests_queue.task_done()

    async def source_worker(self):
        while True:
            if self.requests_queue.qsize() < self.min_queue_size:
                source = await self.sources_queue.get()
                await self.add_source(source)
                self.sources_queue.task_done()
            else:
                await asyncio.sleep(0.05)

    def display_result(self):
        # print(self.store.count_requests_by_state(), end="\x1b[0K\n")
        error_requests = self.store.get_requests_error()
        if error_requests:
            print("Failed requests:", end="\x1b[0K\n")
            for request in error_requests:
                print(request.result(), end="\x1b[0K\n")
