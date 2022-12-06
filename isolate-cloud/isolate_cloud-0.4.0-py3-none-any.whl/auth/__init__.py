from typing import Optional

from dataclasses import dataclass, field
import typer

from isolate_cloud.auth import auth0
from isolate_cloud.auth import local


def login():
    token_data = auth0.login()
    local.save_token(token_data["refresh_token"])


def _fetch_access_token() -> str:
    """
    Load the refresh token, request a new access_token (refreshing the refresh token)
    and return the access_token.

    TODO: We could do this if the access_token is expired (it lasts 1 day),
    instead of every time we invoke.
    """
    refresh_token = local.load_token()

    if refresh_token is None:
        print("Use `isolate-cloud login` flow")
        raise typer.Exit(code=1)

    token_data = auth0.refresh(refresh_token)

    # NOTE: Auth0 Refresh Token Rotation enabled
    # So the old refresh_token is no longer valid
    local.save_token(token_data["refresh_token"])

    return f"{token_data['token_type']} {token_data['access_token']}"


@dataclass
class _User:
    _access_token: Optional[str] = field(repr=False, default=None)
    _user_info: Optional[dict] = field(repr=False, default=None)

    @property
    def info(self) -> dict:
        if self._user_info is None:
            self._user_info = auth0.get_user_info(self.access_token)

        return self._user_info

    @property
    def access_token(self) -> str:
        if self._access_token is None:
            self._access_token = _fetch_access_token()

        return self._access_token


USER = _User()
