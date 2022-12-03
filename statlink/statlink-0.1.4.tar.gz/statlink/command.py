from typing import Tuple

import click

from .crawler import (
    DEFAULT_CONCURRENCY,
    DEFAULT_DEPTH,
    DEFAULT_ENGINE,
    DEFAULT_MAX_RETRY,
    DEFAULT_RATE_LIMIT,
    DEFAULT_TIMEOUT,
    Crawler,
)


@click.command(no_args_is_help=True)
@click.argument("sources", nargs=-1)
@click.option(
    "--concurrency",
    "-c",
    default=DEFAULT_CONCURRENCY,
    show_default=True,
    type=int,
    help="Set the maximum number of concurrent requests.",
)
@click.option(
    "--recursion-mode",
    "-m",
    default="internal",
    show_default=True,
    type=click.Choice(["internal", "all"]),
    help="Set the recursion mode for the crawler.",
)
@click.option(
    "--check-mode",
    default="all",
    show_default=True,
    type=click.Choice(["internal", "all"]),
)
@click.option(
    "--depth",
    "-d",
    default=DEFAULT_DEPTH,
    show_default=True,
    type=int,
    help="Recursion depth value for checking URLs, "
    "negative value will set it to infinity.",
)
@click.option(
    "--timeout",
    "-t",
    default=DEFAULT_TIMEOUT,
    show_default=True,
    type=int,
    help="Set timeout for each requests.",
)
@click.option(
    "--max-retry",
    "-r",
    default=DEFAULT_MAX_RETRY,
    show_default=True,
    type=int,
    help="Set the maximum number of time a request will be retried if failed",
)
@click.option(
    "--engine",
    default=DEFAULT_ENGINE,
    show_default=True,
    type=click.Choice(["aiohttp", "chromium", "firefox", "webkit"]),
    help="Engine that will be used to make requests.",
)
@click.option(
    "--rate-limit",
    "-l",
    default=DEFAULT_RATE_LIMIT,
    show_default=True,
    type=int,
    help="Set the maximum number of requests made per second.",
)
def main(
    sources: Tuple[str],
    concurrency: int,
    recursion_mode: str,
    check_mode: str,
    depth: int,
    timeout: int,
    max_retry: int,
    engine: str,
    rate_limit: int,
) -> None:

    Crawler(
        concurrency=concurrency,
        recursion_mode=recursion_mode,
        check_mode=check_mode,
        depth=depth,
        timeout=timeout,
        max_retry=max_retry,
        engine=engine,
        rate_limit=rate_limit,
    ).start(sources=sources)
