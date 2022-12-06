# coding: utf-8
from typing import TYPE_CHECKING

from .tools import Sensitive

if TYPE_CHECKING:
    from ..._types import StrStrings


class GrantPassword:
    def __init__(
        self, username: str, password: str, token_scope: "StrStrings" = "trapi"
    ):
        """
        Parameters
        ----------
        username: str
            The username to use for authentication
        password: str
            The password to use for authentication
        token_scope: str, list of str (default: trapi)
            The scope to use for authentication

        Examples
        --------
        >>> import refinitiv.data as rdp
        >>> rdp.session.platform.GrantPassword(username="username", password="password", token_scope="token_scope")
        or
        >>> import refinitiv.data as rdp
        >>> rdp.session.platform.GrantPassword("username", "password", "token_scope")

        """
        self._token_scope = token_scope
        self._username = username
        self._password = Sensitive(password)

    def get_username(self):
        return self._username

    def username(self, user_name: str):
        self._username = user_name
        return self

    def get_token_scope(self):
        return self._token_scope

    def with_scope(self, token_scope):
        if token_scope:
            self._token_scope = token_scope
        return self

    def get_password(self):
        return self._password

    def password(self, value: str):
        self._password = Sensitive(value)
        return self

    def is_valid(self):
        return self._password and self._username
