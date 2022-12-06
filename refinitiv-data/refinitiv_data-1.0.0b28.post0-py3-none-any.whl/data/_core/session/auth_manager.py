import threading
import time
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable, Set, Union
from ._scope_map import SCOPE_BY_KEY
from .access_token_updater import AccessTokenUpdater
from .event import UpdateEvent
from .refresh_token_updater import RefreshTokenUpdater
from .tools import MINUTES_10, get_delays
from ..log_reporter import LogReporter
from ..._errors import ScopeError
from ..._tools import cached_property, CallbackHandler

if TYPE_CHECKING:
    from ._platform_session import PlatformSession

DEFAULT_EXPIRES_IN_SEC = MINUTES_10
DEFAULT_LATENCY_SEC = 20

delays = get_delays()


@dataclass
class TokenInfo:
    access_token: str = ""
    expires_in: Union[float, str] = 0
    expires_at: float = field(init=False)
    scope: Set[str] = field(default_factory=set)
    token_type: str = ""
    refresh_token: str = ""

    def __post_init__(self):
        self.expires_in = self.calc_expires_in(self.expires_in)
        self.expires_at = time.time() + self.expires_in

    @staticmethod
    def calc_expires_in(expires_in: Union[float, str]) -> float:
        try:
            expires_in = float(expires_in)
        except ValueError:
            expires_in = DEFAULT_EXPIRES_IN_SEC
        return max(expires_in, DEFAULT_EXPIRES_IN_SEC)

    def calc_token_update_time(self, latency: float) -> int:
        latency = min(latency, DEFAULT_LATENCY_SEC)

        expires_secs = self.expires_in / 2

        if expires_secs - latency > 0:
            expires_secs = expires_secs - latency

        return int(expires_secs)

    @classmethod
    def from_dict(cls, json_content: dict) -> "TokenInfo":
        return cls(
            access_token=json_content["access_token"],
            refresh_token=json_content["refresh_token"],
            expires_in=json_content.get("expires_in", ""),
            scope=set(json_content.get("scope", "").split()),
            token_type=json_content.get("token_type", ""),
        )

    def update(self, other: "TokenInfo") -> None:
        self.access_token = other.access_token
        self.refresh_token = other.refresh_token
        self.expires_in = other.expires_in
        self.expires_at = other.expires_at
        self.scope = other.scope
        self.token_type = other.token_type


class AuthManager(LogReporter):
    """
    Methods
    -------
    is_closed()
        The method returns True if closed, otherwise False

    is_authorized()
        The method returns True if authorized, otherwise False.
        If instance destroyed or closed always returns False

    authorize()
        The method starts process authorization

    close()
        The method stops refresh token updater and access token updater

    dispose()
        The method destroy an instance

    """

    def __init__(self, session: "PlatformSession", auto_reconnect: bool) -> None:
        LogReporter.__init__(self, logger=session)

        self._session = session
        self._auto_reconnect = auto_reconnect

        self._ee = CallbackHandler()
        self._token_info = TokenInfo()

        self._closed: bool = False
        self._authorized: bool = False
        self._disposed: bool = False

        self._result_evt: threading.Event = threading.Event()
        self._start_evt: threading.Event = threading.Event()
        self._thread: threading.Thread = threading.Thread(
            target=self._do_authorize,
            name="AuthManager-Thread",
            daemon=True,
        )

    @cached_property
    def _access_token_updater(self) -> AccessTokenUpdater:
        return AccessTokenUpdater(
            self._session,
            0.00001,
            self._access_token_update_handler,
        )

    @cached_property
    def _refresh_token_updater(self) -> RefreshTokenUpdater:
        return RefreshTokenUpdater(
            self._session,
            self._token_info,
            0.00001,
            self._refresh_token_update_handler,
        )

    def on(self, event: str, listener: Callable):
        self._ee.on(event, listener)

    def is_closed(self) -> bool:
        """

        Returns
        -------
        bool
            True if closed, otherwise False
        """
        return self._closed is True

    def is_authorized(self) -> bool:
        """

        Returns
        -------
        bool
            True if authorized, otherwise False
        """
        if self.is_closed():
            return False

        return self._authorized is True

    def authorize(self) -> bool:
        """
        The method starts process authorization

        Returns
        -------
        bool
            True if authorized, otherwise False
        """
        if self._disposed:
            raise RuntimeError("AuthManager disposed")

        if self.is_authorized():
            return True

        self.debug("AuthManager: start authorize")

        self._closed = False
        self._authorized = False

        self._result_evt.clear()
        self._start_evt.set()

        if not self._thread.ident:
            self._thread.start()

        self._result_evt.wait()

        is_authorized = self.is_authorized()
        self.debug(f"AuthManager: end authorize, result {is_authorized}")
        return is_authorized

    def _do_authorize(self):
        while not self._disposed:

            self._start_evt.wait()

            if self._disposed:
                break

            self.debug(
                f"AuthManager: Access token will be requested "
                f"in {self._access_token_updater.delay} seconds"
            )
            self._access_token_updater.start()

            if self.is_authorized():
                latency_secs = self._access_token_updater.latency_secs
                delay = self._token_info.calc_token_update_time(latency_secs)
                self._refresh_token_updater.delay = delay
                self.debug(
                    f"AuthManager: Refresh token will be requested "
                    f"in {self._refresh_token_updater.delay} seconds"
                )
                self._refresh_token_updater.start()

    def close(self):
        """
        The method stops refresh token updater and access token updater

        Returns
        -------
        None
        """
        if self._disposed:
            raise RuntimeError("AuthManager disposed")

        if self.is_closed():
            return

        self.debug("AuthManager: close")
        self._ee.emit(UpdateEvent.CLOSE_AUTH_MANAGER, self)
        self._start_evt.clear()
        self._access_token_updater.stop()
        self._refresh_token_updater.stop()
        self._closed = True
        self._authorized = False

    def _access_token_update_handler(
        self, event: str, message: str, json_content: dict
    ) -> None:
        self.debug(
            f"AuthManager: Access token handler, event: {event}, message: {message}"
        )

        if event is UpdateEvent.ACCESS_TOKEN_SUCCESS:
            self._authorized = True
            delays.reset()
            token_info = TokenInfo.from_dict(json_content)
            self._token_info.update(token_info)
            access_token = self._token_info.access_token
            self.debug(
                f"Access token {access_token}. "
                f"Expire in {self._token_info.expires_in} seconds"
            )
            self._ee.emit(UpdateEvent.UPDATE_ACCESS_TOKEN, access_token)
            self._access_token_updater.stop()
            self._ee.emit(event, message)
            self._ee.emit(UpdateEvent.AUTHENTICATION_SUCCESS, message)
            self._result_evt.set()

        elif event is UpdateEvent.ACCESS_TOKEN_UNAUTHORIZED:
            self._authorized = False
            self._access_token_updater.stop()
            self._ee.emit(event, message)
            self._ee.emit(UpdateEvent.AUTHENTICATION_FAILED, message)
            self.close()
            self._result_evt.set()

        elif event is UpdateEvent.ACCESS_TOKEN_FAILED:
            if not self._auto_reconnect:
                self._authorized = False
                self._access_token_updater.stop()
                self._result_evt.set()

            self._ee.emit(event, message)
            self._ee.emit(UpdateEvent.AUTHENTICATION_FAILED, message)

            if self._auto_reconnect:
                delay = delays.next()
                self.debug(f"AuthManager: reconnecting in {delay} secs")
                self._access_token_updater.delay = delay
                self._ee.emit(UpdateEvent.RECONNECTING, message)

            else:
                self.close()

    def _refresh_token_update_handler(
        self, event: str, message: str, json_content: dict
    ) -> None:
        self.debug(
            f"AuthManager: Refresh token handler, event: {event}, message: {message}"
        )

        if event is UpdateEvent.REFRESH_TOKEN_SUCCESS:
            token_info = TokenInfo.from_dict(json_content)
            self._token_info.update(token_info)
            access_token = token_info.access_token
            self.debug(
                f"Received access token {token_info.refresh_token}. "
                f"Expire in {token_info.expires_in} seconds"
            )
            self._ee.emit(UpdateEvent.UPDATE_ACCESS_TOKEN, access_token)
            latency_secs = self._access_token_updater.latency_secs
            delay = token_info.calc_token_update_time(latency_secs)
            self._refresh_token_updater.delay = delay
            self.debug(f"Set refresh token delay to {delay} seconds")
            self._ee.emit(event, message)

        elif event is UpdateEvent.REFRESH_TOKEN_BAD:
            self._authorized = False
            self._ee.emit(event, message)
            self._ee.emit(UpdateEvent.AUTHENTICATION_FAILED, message)
            self.close()

        elif event is UpdateEvent.REFRESH_TOKEN_FAILED:
            self._ee.emit(event, message)
            self._ee.emit(UpdateEvent.AUTHENTICATION_FAILED, message)

            if self._auto_reconnect:
                delay = delays.next()
                self.debug(
                    f"AuthManager: Trying to get Refresh token again in {delay} secs"
                )
                self._refresh_token_updater.delay = delay
                self._ee.emit(UpdateEvent.RECONNECTING, message)

            else:
                self._authorized = False
                self.close()

        elif event is UpdateEvent.REFRESH_TOKEN_EXPIRED:
            self._ee.emit(event, message)
            self._ee.emit(UpdateEvent.AUTHENTICATION_FAILED, message)
            self._authorized = False

            if self._auto_reconnect:
                self.debug("AuthManager: reconnecting")
                self._ee.emit(UpdateEvent.RECONNECTING, message)
                self._refresh_token_updater.stop()

            else:
                self.close()

    def dispose(self):
        """
        The method destroy an instance

        Returns
        -------
        None
        """
        if self._disposed:
            return

        if not self.is_closed():
            self.close()

        self._disposed = True
        self._access_token_updater.dispose()
        self._refresh_token_updater.dispose()
        self._start_evt.set()
        self._ee.remove_all_listeners()
        self._ee = None
        self._token_info = None
        self._start_evt = None
        self._thread = None
        self._session = None

    def verify_scope(self, key: str, method: str):
        required_scope_sets = SCOPE_BY_KEY.get((key.rstrip("/"), method.lower()))

        if required_scope_sets is None:
            self.debug(f"Scope for key={key}, method={method} not found.")

        if required_scope_sets and all(
            not required_scope.issubset(self._token_info.scope)
            for required_scope in required_scope_sets
        ):
            self.warning(f"No user scope for key={key}, method={method}.")
            raise ScopeError(required_scope_sets, self._token_info.scope, key, method)
