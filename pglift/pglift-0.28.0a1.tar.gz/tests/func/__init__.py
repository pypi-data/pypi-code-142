import enum
from contextlib import contextmanager
from functools import partial
from typing import Any, Dict, Iterator, List, Literal, Optional, overload
from unittest.mock import patch

import psycopg
import pytest

from pglift import db, instances, postgresql
from pglift.ctx import Context
from pglift.models import interface, system
from pglift.types import ConfigChanges, Role


class AuthType(str, enum.Enum):
    peer = "peer"
    password_command = "password_command"
    pgpass = "pgpass"


@contextmanager
def reconfigure_instance(
    ctx: Context,
    manifest: interface.Instance,
    port: Optional[int] = None,
    **confitems: Any,
) -> Iterator[ConfigChanges]:
    """Context manager to temporarily change instance settings.

    Upon enter, this applies provided settings (and possibly new port)
    and yields settings 'changes' dict.

    Upon exit, the previous settings is restored, and the 'changes' dict
    returned upon enter is updated to reflect this.
    """
    update: Dict[str, Any] = {}
    if port is not None:
        update["port"] = port
    if confitems:
        update["settings"] = dict(manifest.settings.copy(), **confitems)
    assert update
    changes = instances.configure(ctx, manifest._copy_validate(update))
    try:
        yield changes
    finally:
        restored_changes = instances.configure(ctx, manifest)
        changes.clear()
        changes.update(restored_changes)


@overload
def execute(
    ctx: Context,
    instance: system.Instance,
    query: str,
    fetch: Literal[True],
    role: Optional[Role] = None,
    **kwargs: Any,
) -> List[Any]:
    ...


@overload
def execute(
    ctx: Context,
    instance: system.Instance,
    query: str,
    fetch: bool = False,
    role: Optional[Role] = None,
    **kwargs: Any,
) -> List[Any]:
    ...


def execute(
    ctx: Context,
    instance: system.Instance,
    query: str,
    fetch: bool = True,
    role: Optional[Role] = None,
    **kwargs: Any,
) -> Optional[List[Any]]:
    if role is None:
        connect = partial(db.connect, ctx)
    elif role.password:
        connect = partial(
            db.connect,
            ctx,
            user=role.name,
            password=role.password.get_secret_value(),
        )
    else:
        connect = partial(db.connect, settings=ctx.settings.postgresql, user=role.name)
    with postgresql.running(ctx, instance):
        with connect(instance, **kwargs) as conn:
            cur = conn.execute(query)
            if fetch:
                return cur.fetchall()
        return None


def check_connect(
    ctx: Context,
    postgresql_auth: AuthType,
    instance_manifest: interface.Instance,
    instance: system.Instance,
) -> None:
    surole = instance_manifest.surole(ctx.settings)
    port = instance.port
    connargs = {
        "host": str(instance.config().unix_socket_directories),
        "port": port,
        "user": surole.name,
    }
    if postgresql_auth == AuthType.peer:
        pass
    elif postgresql_auth == AuthType.pgpass:
        connargs["passfile"] = str(ctx.settings.postgresql.auth.passfile)
    else:
        with pytest.raises(
            psycopg.OperationalError, match="no password supplied"
        ) as exc_info:
            with patch.dict("os.environ", clear=True):
                psycopg.connect(**connargs).close()  # type: ignore[call-overload]
        assert exc_info.value.pgconn
        assert exc_info.value.pgconn.needs_password
        assert surole.password is not None
        connargs["password"] = surole.password.get_secret_value()
    with psycopg.connect(**connargs) as conn:  # type: ignore[call-overload]
        if postgresql_auth == AuthType.peer:
            assert not conn.pgconn.used_password
        else:
            assert conn.pgconn.used_password
