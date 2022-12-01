import datetime
import random
import time
from email.utils import parsedate_to_datetime
from typing import FrozenSet, Set

import httpx

from .middleware import BaseMiddleware
from .options import RetryHandlerOption


class RetryHandler(BaseMiddleware):
    """
    Middleware that allows us to specify the retry policy for all requests
    Retry configuration.
    :param int max_retries:
        Maximum number of retries to allow. Takes precedence over other counts.
        Set to ``0`` to fail on the first retry.
    :param iterable retry_on_status_codes:
        A set of integer HTTP status codes that we should force a retry on.
        A retry is initiated if the request method is in ``allowed_methods``
        and the response status code is in ``RETRY STATUS CODES``.
    :param float retry_backoff_factor:
        A backoff factor to apply between attempts after the second try
        (most errors are resolved immediately by a second try without a
        delay).
        The request will sleep for::
            {backoff factor} * (2 ** ({retry number} - 1))
        seconds. If the backoff_factor is 0.1, then :func:`.sleep` will sleep
        for [0.0s, 0.2s, 0.4s, ...] between retries. It will never be longer
        than :attr:`RetryHandler.MAXIMUM_BACKOFF`.
        By default, backoff is set to 0.5.
    :param int retry_time_limit:
        The maximum cumulative time in seconds that total retries should take.
        The cumulative retry time and retry-after value for each request retry
        will be evaluated against this value; if the cumulative retry time plus
        the retry-after value is greater than the retry_time_limit, the failed
        response will be immediately returned, else the request retry continues.
    """
    DEFAULT_BACKOFF_FACTOR: float = 0.5

    MAXIMUM_BACKOFF: int = 120

    # A list of status codes that needs to be retried
    # 429 - Too many requests
    # 503 - Service unavailable
    # 504 - Gateway timeout
    DEFAULT_RETRY_STATUS_CODES: Set[int] = {429, 503, 504}

    DEFAULT_ALLOWED_METHODS: FrozenSet[str] = frozenset(
        ['HEAD', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
    )

    def __init__(self, options: RetryHandlerOption = RetryHandlerOption()) -> None:
        super().__init__()
        self.max_retries: int = options.max_retry  #type: ignore
        self.backoff_factor: float = self.DEFAULT_BACKOFF_FACTOR
        self.backoff_max: int = self.MAXIMUM_BACKOFF
        self.timeout: float = options.max_delay
        self.retry_on_status_codes: Set[int] = self.DEFAULT_RETRY_STATUS_CODES
        self.allowed_methods: FrozenSet[str] = self.DEFAULT_ALLOWED_METHODS
        self.retries_allowed: bool = options.should_retry
        self.respect_retry_after_header: bool = options.DEFAULT_SHOULD_RETRY

    async def send(self, request: httpx.Request, transport: httpx.AsyncBaseTransport):
        """
        Sends the http request object to the next middleware or retries the request if necessary.
        """
        response = None
        retry_count = 0
        retry_valid = self.retries_allowed

        while retry_valid:
            start_time = time.time()
            if retry_count > 0:
                request.headers.update({'retry-attempt': f'{retry_count}'})
            response = await super().send(request, transport)
            # Check if the request needs to be retried based on the response method
            # and status code
            if self.should_retry(request, response):
                # check that max retries has not been hit
                retry_valid = self.check_retry_valid(retry_count)

                # Get the delay time between retries
                delay = self.get_delay_time(retry_count, response)

                if retry_valid and delay < self.timeout:
                    time.sleep(delay)
                    end_time = time.time()
                    self.timeout -= (end_time - start_time)
                    # increment the count for retries
                    retry_count += 1

                    continue
            break
        return response

    def should_retry(self, request, response):
        """
        Determines whether the request should be retried
        Checks if the request method is in allowed methods
        Checks if the response status code is in retryable status codes.
        """
        if not self._is_method_retryable(request):
            return False
        if not self._is_request_payload_buffered(request):
            return False
        val = self.max_retries and (response.status_code in self.retry_on_status_codes)
        return val

    def _is_method_retryable(self, request):
        """
        Checks if a given request should be retried upon, depending on
        whether the HTTP method is in the set of allowed methods
        """
        if request.method.upper() not in self.allowed_methods:
            return False
        return True

    def _is_request_payload_buffered(self, request):
        """
        Checks if the request payload is buffered/rewindable.
        Payloads with forward only streams will return false and have the responses
        returned without any retry attempt.
        """
        if request.method.upper() in frozenset(['HEAD', 'GET', 'DELETE', 'OPTIONS']):
            return True
        if request.headers.get('Content-Type') == "application/octet-stream":
            return False
        return True

    def check_retry_valid(self, retry_count):
        """
        Check that the max retries limit has not been hit
        """
        if retry_count < self.max_retries:
            return True
        return False

    def get_delay_time(self, retry_count, response=None):
        """
        Get the time in seconds to delay between retry attempts.
        Respects a retry-after header in the response if provided
        If no retry-after response header, it defaults to exponential backoff
        """
        retry_after = self._get_retry_after(response)
        if retry_after:
            return retry_after
        return self._get_delay_time_exp_backoff(retry_count)

    def _get_delay_time_exp_backoff(self, retry_count):
        """
        Get time in seconds to delay between retry attempts based on an exponential
        backoff value.
        """
        exp_backoff_value = self.backoff_factor * +(2**(retry_count - 1))
        backoff_value = exp_backoff_value + (random.randint(0, 1000) / 1000)

        backoff = min(self.backoff_max, backoff_value)
        return backoff

    def _get_retry_after(self, response):
        """
        Check if retry-after is specified in the response header and get the value
        """
        retry_after = response.headers.get("retry-after")
        if retry_after:
            return self._parse_retry_after(retry_after)
        return None

    def _parse_retry_after(self, retry_after):
        """
        Helper to parse Retry-After and get value in seconds.
        """
        try:
            delay = int(retry_after)
        except ValueError:
            # Not an integer? Try HTTP date
            retry_date = parsedate_to_datetime(retry_after)
            delay = (retry_date - datetime.datetime.now(retry_date.tzinfo)).total_seconds()
        return max(0, delay)
