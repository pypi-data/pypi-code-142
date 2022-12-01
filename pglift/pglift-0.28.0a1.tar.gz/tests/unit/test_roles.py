from typing import Optional

import pytest
from pydantic import SecretStr

from pglift import exceptions, roles
from pglift.ctx import Context
from pglift.models import interface
from pglift.models.system import Instance


class Role(interface.Role):
    def __init__(
        self, name: str, password: Optional[str] = None, pgpass: bool = False
    ) -> None:
        super().__init__(
            name=name,
            password=SecretStr(password) if password is not None else None,
            pgpass=pgpass,
        )


def test_in_pgpass(ctx: Context, instance: Instance) -> None:
    fpath = ctx.settings.postgresql.auth.passfile
    fpath.write_text("*:999:*:edgar:fbi\n")
    assert roles.in_pgpass(ctx, instance, "edgar")
    assert not roles.in_pgpass(ctx, instance, "alice")


def test_standby_role_create(ctx: Context, standby_instance: Instance) -> None:
    role = Role("alice")
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby instance$",
    ):
        roles.create(ctx, standby_instance, role)


def test_standby_role_drop(ctx: Context, standby_instance: Instance) -> None:
    role = Role("alice")
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby instance$",
    ):
        roles.drop(ctx, standby_instance, role)


def test_standby_role_alter(ctx: Context, standby_instance: Instance) -> None:
    role = Role("alice")
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby instance$",
    ):
        roles.alter(ctx, standby_instance, role)


def test_standby_set_password_for(ctx: Context, standby_instance: Instance) -> None:
    role = Role("alice")
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby instance$",
    ):
        roles.set_password_for(ctx, standby_instance, role)
