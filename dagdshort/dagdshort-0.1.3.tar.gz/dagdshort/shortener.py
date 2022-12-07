"""URL shortener."""
import base64
import binascii
import concurrent.futures
import functools
import logging
import random
import socket
import threading
import time
import types
from urllib.parse import urlparse

import requests

from . import config, exc

log = logging.getLogger(__name__)


class Shortener:
    """Shortener."""

    def __init__(self, *, user_agent_suffix: str, max_cache_size: int = config.DEFAULT_CACHE_SIZE):
        self._user_agent_suffix = user_agent_suffix
        self._max_cache_size = max_cache_size
        self._check_args()

        self._shorten_url = functools.lru_cache(maxsize=self._max_cache_size)(self._shorten_url)  # type: ignore  # Instance level cache
        self._init_executor()
        if config.TEST_API_ON_INIT:
            self._test()

    def _cache_state(self) -> str:
        cache_info = self._shorten_url.cache_info()  # type: ignore
        calls = cache_info.hits + cache_info.misses
        hit_percentage = ((100 * cache_info.hits) / calls) if (calls != 0) else 0
        size_percentage = ((100 * cache_info.currsize) / cache_info.maxsize) if cache_info.maxsize else 100
        cache_state = f"Cache state is: hits={cache_info.hits}, currsize={cache_info.currsize}, " f"hit_rate={hit_percentage:.0f}%, size_rate={size_percentage:.0f}%"
        return cache_state

    def _check_args(self) -> None:
        # Check max workers
        if (not (isinstance(config.MAX_WORKERS, int))) or (not (1 <= config.MAX_WORKERS <= 32)):
            raise exc.ArgsError(f"Max workers must be an integer between 1 and 32, but it is {config.MAX_WORKERS}.")
        log.debug(f"Max workers is {config.MAX_WORKERS}.")

        # Check user agent suffix
        ua_suffix = self._user_agent_suffix
        if (not (isinstance(ua_suffix, str))) or (not (1 <= len(ua_suffix) <= 512)) or (ua_suffix != ua_suffix.strip()):
            raise exc.ArgsError(f"User agent suffix must be a non-empty whitespace-stripped string having length between 1 and 512, but it is {ua_suffix}.")
        log.debug(f"User agent suffix is {ua_suffix}.")

        # Check max cache size
        max_cache_size = self._max_cache_size
        if (not (isinstance(max_cache_size, int))) or (max_cache_size < 0):
            raise exc.ArgsError(f"Max cache size must be a non-negative integer, but it is {max_cache_size}.")
        log.debug(f"Max cache size is {max_cache_size}.")

    @staticmethod
    def _check_long_urls(long_urls: list[str]) -> None:
        if not ((isinstance(long_urls, (list, tuple))) and all(isinstance(long_url, str) for long_url in long_urls)):
            raise exc.ArgsError(f"The given argument must be a list of URL strings. It is of type {type(long_urls)}.")

    def _init_requests_session(self) -> None:
        self._thread_local.session_post = requests.Session()
        log.debug("Initialized requests session.")

    def _init_executor(self) -> None:
        self._thread_local = threading.local()
        self._init_requests_session()  # For conditional non-parallel execution.
        self._executor = concurrent.futures.ThreadPoolExecutor(  # pylint: disable=consider-using-with
            max_workers=config.MAX_WORKERS, thread_name_prefix="Requester", initializer=self._init_requests_session
        )
        log.debug("Initialized thread pool executor.")

    @staticmethod
    def _is_known_short_url(url: str) -> bool:
        result = urlparse(url)
        return (result.netloc in config.KNOWN_SHORT_DOMAINS) and (result.scheme in {"https", "http"})

    def _shorten_url(self, long_url: str) -> str:  # pylint: disable=too-many-locals,method-hidden
        assert long_url == long_url.strip()
        if self._is_known_short_url(long_url):
            short_url = long_url
        else:
            # Shorten long URL
            for num_attempt in range(1, config.MAX_ATTEMPTS + 1):
                sleep_time = random.random() * (num_attempt - 1)  # Is 0 for first attempt.
                if sleep_time > 0:
                    log.debug(f"Sleeping for {sleep_time:.1f}s for attempt {num_attempt} of {config.MAX_ATTEMPTS} for long URL {long_url}.")
                    time.sleep(sleep_time)
                response_desc = f"response for long URL {long_url} in attempt {num_attempt} of {config.MAX_ATTEMPTS}"
                try:
                    log.debug(f"Requesting {response_desc}.")
                    start_time = time.monotonic()
                    status_desc = f"Failed to receive a {response_desc}."  # For use with exception handling.
                    response = types.SimpleNamespace(status_code="(undefined)")  # For use with exception handling.
                    response = self._thread_local.session_post.post(  # Ref: https://github.com/dagd/dagd/issues/49
                        url=config.API_URL_SHORTEN,
                        data={"url": long_url, "strip": True},
                        allow_redirects=False,
                        timeout=config.REQUEST_TIMEOUT,
                        headers={"User-Agent": self._user_agent},
                    )  # Note: This too can raise an exception, such as in case of a timeout.
                    time_used = time.monotonic() - start_time
                    status_desc = f"Received {response_desc} having status code {response.status_code} in {time_used:.1f}s: {response.text}"
                    log.debug(status_desc)
                    response.raise_for_status()
                    break
                except requests.RequestException as exception:
                    exc_desc = f"{status_desc} The exception is: {exception.__class__.__qualname__}: {exception}"
                    log.warning(exc_desc)
                    if num_attempt == config.MAX_ATTEMPTS:
                        error_msg = f" Exhausted all {config.MAX_ATTEMPTS} attempts. {exc_desc}"
                        raise exc.RequestError(error_msg) from None
                    if response.status_code == 400:
                        error_msg = f"Retry aborted. {exc_desc}"
                        raise exc.RequestError(error_msg) from None
            assert response.status_code == 200
            short_url = response.text
            assert short_url == short_url.strip()

        # Postprocess short URL
        if short_url.startswith("http://"):  # Example: http://da.gd/help
            short_url = short_url.replace("http://", "https://", 1)

        log.debug(f"Returning short URL {short_url} for long URL {long_url}.")
        return short_url

    @functools.cached_property
    def _user_agent(self) -> str:
        base_repo_name = pseudo_salt = config.BASE_REPO_NAME
        hostname_salted = f"{socket.gethostname()}; {pseudo_salt}"  # Intended only to prevent a casual lookup in a search engine.
        hostname_digest = binascii.crc32(hostname_salted.encode()).to_bytes(4, "big")  # Ref: https://stackoverflow.com/a/68883969/
        hostname_digest_encoded = base64.b16encode(hostname_digest).decode().lower()
        user_agent = f"host={hostname_digest_encoded}; basepkg={base_repo_name}; userpkg={self._user_agent_suffix}"
        log.info(f"Request user agent for URL shortener is: {user_agent}")
        return user_agent

    def _test(self) -> None:
        long_url = config.TEST_LONG_URL
        log.debug(f"Testing API for long URL {long_url}.")
        short_url = self.shorten_urls([long_url])[long_url]
        log.debug(f"Tested API for long URL {long_url}. Received short URL {short_url}.")

    @property
    def cache_info(self) -> dict[str, functools._CacheInfo]:
        """Return cache info."""
        source = self._shorten_url
        return {source.__qualname__: source.cache_info()}  # type: ignore

    def shorten_urls(self, long_urls: list[str]) -> dict[str, str]:
        """Return a dictionary mapping the given long URLs to their respective short URLs.

        If a given URL is already a known short URL, it is returned unchanged.

        `dagdshort.exc.RequestError` is raised if the request fails despite multiple attempts.
        """
        self._check_long_urls(long_urls)
        num_urls = len(long_urls)
        if ((len(set(long_urls)) > 1) and (config.MAX_WORKERS > 1)) or (not (hasattr(self._thread_local, "session_post"))):  # Note: The hasattr check handles a bug.
            num_workers = min(num_urls, config.MAX_WORKERS)
            strategy_desc = f"concurrently using {num_workers} workers"
            url_mapper = self._executor.map
        else:
            strategy_desc = "serially"
            url_mapper = map  # type: ignore
        log.debug(f"Retrieving {num_urls} short URLs {strategy_desc}.")
        start_time = time.monotonic()
        url_map = dict(url_mapper(lambda long_url: (long_url, self._shorten_url(long_url.strip())), long_urls))
        time_used = time.monotonic() - start_time
        assert num_urls == len(url_map)
        rate_per_second = (num_urls / time_used) if (time_used != 0) else float("inf")
        log.info(f"Retrieved {num_urls} short URLs {strategy_desc} in {time_used:.1f}s at a rate of {rate_per_second:,.0f}/s. {self._cache_state()}")
        return url_map
