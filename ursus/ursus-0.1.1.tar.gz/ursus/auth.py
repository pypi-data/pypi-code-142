import functools
import os
from abc import ABC, abstractmethod
from typing import Awaitable, Callable, Optional, ParamSpec, TypeVar, cast

import quart

from .utils import ViewFuncReturnT


_T = TypeVar('_T')
_P = ParamSpec('_P')


class BaseUser(ABC):
    username: str
    domains: list[tuple[str, bool]]

    def __init__(self, username: str, domains: list[tuple[str, bool]]):
        self.username = username
        self.domains = domains.copy()

    @abstractmethod
    def is_authenticated(self) -> bool:
        ...


class User(BaseUser):
    def is_authenticated(self) -> bool:
        return True


class AnonymousUser(BaseUser):
    def __init__(self, username: str = '', domains: list[tuple[str, bool]] = []):
        super().__init__('anonymous', [])

    def is_authenticated(self) -> bool:
        return False


class AuthManager:
    def __init__(self, app: Optional[quart.Quart] = None):
        if app:
            self.init_app(app)

    def init_app(self, app: quart.Quart) -> None:
        app.jinja_env.globals['current_user'] = self.current_user

    @classmethod
    def parse_domains(cls, domain_str: str) -> list[tuple[str, bool]]:
        """Parse domains in the format "domain1/is_admin:domain2/is_admin".

        where `is_admin` is a `0` (False, not admin) or a `1` (True, is admin).
        """
        domains = []

        for domain_and_is_admin in domain_str.split(':'):
            domain, is_admin_str = domain_and_is_admin.split('/')

            if is_admin_str == '0':
                is_admin = False
            elif is_admin_str == '1':
                is_admin = True
            else:
                raise ValueError(f'malformed domain list: wanted `0` or `1` got `{is_admin_str}`')

            domains.append((domain, is_admin))

        return domains

    async def current_user(self) -> BaseUser:
        if getattr(quart.g, 'current_user', None):
            return cast(BaseUser, quart.g.current_user)

        username = os.environ.get('HTTP_USERNAME')
        if username is None:
            return AnonymousUser()

        unpased_domains = os.environ.get('URSUS_DOMAINS', '')

        domains = AuthManager.parse_domains(unpased_domains)

        quart.g.current_user = User(username, domains)
        return quart.g.current_user

    def login_required(
        self,
        view_func: Callable[_P, Awaitable[ViewFuncReturnT]]
    ) -> Callable[_P, Awaitable[ViewFuncReturnT]]:
        @functools.wraps(view_func)
        async def inner(*args: _P.args, **kwargs: _P.kwargs) -> ViewFuncReturnT:
            if (await self.current_user()).is_authenticated():
                return await view_func(*args, **kwargs)
            else:
                # TODO: redirect to where a user can auth
                return quart.redirect(quart.url_for('index'))

        return inner
