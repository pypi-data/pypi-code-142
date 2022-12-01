"""Library for connecting to RIME backend services."""

import logging
from typing import Any, Callable, Dict, Generic, Optional, TypeVar

import grpc

from rime_sdk.internal.client_interceptor import (
    AddMetadataUnaryStreamClientInterceptor,
    AddMetadataUnaryUnaryClientInterceptor,
)

logger = logging.getLogger()

# Generic type representing a client stub for a gRPC server.
C = TypeVar("C")


class RIMEConnection(Generic[C]):
    """A connection to a backend client of type C."""

    def __init__(
        self,
        create_backend_fn: Callable[..., C],
        addr: str,
        api_key: str,
        channel_timeout: float = 5.0,
        disable_tls: bool = False,
        ssl_config: Optional[Dict[str, str]] = None,
    ) -> None:
        """Create a new connection for a RIME backend.

        Args:
            create_backend_fn: Callable[..., C]
                Function to create a backend of type C from the channel acquired for
                this connection.
            addr: str
                The address of the backend server to create a channel to.
            api_key: str
                Api Key to validate RIME grpc requests with.
            channel_timeout: float
                The timeout in seconds for waiting for the given channel.
            disable_tls: bool
                Whether to disable tls when connecting to the backend.
            ssl_config: dict(str)
                SSL config to be passed to grpc.ssl_channel_credentials. Documentation
                can be found here: https://grpc.github.io/grpc/python/_modules/grpc.html#ssl_channel_credentials
        """
        self._create_backend_fn = create_backend_fn
        self._api_key = api_key
        self._addr = addr
        self._channel_timeout = channel_timeout
        self._channel: Optional[grpc.Channel] = None
        self._disable_tls = disable_tls
        self._ssl_config = ssl_config if ssl_config is not None else {}

    def __enter__(self) -> C:
        """Acquires the channel created in the with-context."""
        self._channel = self._build_and_validate_channel(
            self._addr, self._channel_timeout
        )
        return self._create_backend_fn(self._channel)

    def __exit__(self, exc_type: Any, exc_value: Any, exc_traceback: Any) -> None:
        """Frees the channel created in the with-context.

        Args:
            exc_type: Any
                The type of the exception (None if no exception occurred).
            exc_value: Any
                The value of the exception (None if no exception occurred).
            exc_traceback: Any
                The traceback of the exception (None if no exception occurred).
        """
        if self._channel:
            self._channel.close()

    def _build_and_validate_channel(self, addr: str, timeout: float,) -> grpc.Channel:
        """Build and validate a secure gRPC channel at `addr`.

        Args:
            addr: str
                The address of the RIME gRPC service.
            timeout: float
                The amount of time in seconds to wait for the channel to become ready.

        Raises:
            ValueError
                If a connection cannot be made to a backend service within `timeout`.
        """

        try:
            # create credentials
            if self._disable_tls:
                channel = grpc.insecure_channel(addr)
            else:
                credentials = self._get_ssl_channel_credentials()
                channel = grpc.secure_channel(addr, credentials)
            channel = grpc.intercept_channel(
                channel,
                AddMetadataUnaryUnaryClientInterceptor(self._api_key),
                AddMetadataUnaryStreamClientInterceptor(self._api_key),
            )
            grpc.channel_ready_future(channel).result(timeout=timeout)
            return channel
        except grpc.FutureTimeoutError:
            raise ValueError(
                f"Could not connect to server at address `{addr}`. "
                "Please confirm the URL is correct and check your network connection."
            ) from None

    def _get_ssl_channel_credentials(self) -> grpc.ChannelCredentials:
        """Fetch channel credentials for an SSL channel."""
        return grpc.ssl_channel_credentials(**self._ssl_config)


class RIMEBackend:
    """An abstraction for connecting to RIME's backend services."""

    def __init__(
        self,
        domain: str,
        api_key: str = "",
        channel_timeout: float = 5.0,
        disable_tls: bool = False,
        ssl_config: Optional[Dict[str, str]] = None,
    ):
        """Create a new RIME backend.

        Args:
            domain: str
                The backend domain/address of the RIME service.
            api_key: str
                The api key providing authentication to RIME services
            channel_timeout: float
                The amount of time in seconds to wait for channels to become ready
                when opening connections to gRPC servers.
            disable_tls: bool
                Whether to disable tls when connecting to the backend.
            ssl_config: dict(str)
                SSL config to be passed to grpc.ssl_channel_credentials. Documentation
                can be found here: https://grpc.github.io/grpc/python/_modules/grpc.html#ssl_channel_credentials
        """
        self._channel_timeout = channel_timeout
        self._api_key = api_key
        self._disable_tls = disable_tls
        domain_split = domain.split(".", 1)
        self._ssl_config = ssl_config if ssl_config is not None else {}
        if domain_split[0][-4:] == "rime":
            base_domain = domain_split[1]
            domain = "rime-backend." + base_domain
        if domain.endswith("/"):
            domain = domain[:-1]
        self._backend_addr = self._get_backend_addr(domain, disable_tls)
        # Make sure this is last as it is dependent on connections being configured.

    def _get_backend_addr(self, domain: str, disable_tls: bool = False) -> str:
        """Construct an address to the all backend services from `domain`.

        Args:
            domain: str
                The backend domain/address of the RIME service.
            disable_tls: bool
                Whether to disable tls when connecting to the backend.
        """
        if disable_tls:
            return f"{domain}:80"
        return f"{domain}:443"
