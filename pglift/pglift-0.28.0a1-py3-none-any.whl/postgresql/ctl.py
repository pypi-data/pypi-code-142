import functools
import logging
import time
from decimal import Decimal
from pathlib import Path
from typing import TYPE_CHECKING, Optional

import psycopg
from pgtoolkit import ctl
from pgtoolkit.ctl import Status

from .. import db, exceptions
from ..settings import PostgreSQLVersion

if TYPE_CHECKING:

    from ..ctx import Context
    from ..models.system import BaseInstance, PostgreSQLInstance

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=len(PostgreSQLVersion) + 1)
def pg_ctl(bindir: Path, *, ctx: "Context") -> ctl.PGCtl:
    return ctl.PGCtl(bindir, run_command=ctx.run)


def is_ready(ctx: "Context", instance: "PostgreSQLInstance") -> bool:
    """Return True if the instance is ready per pg_isready."""
    logger.debug("checking if PostgreSQL instance %s is ready", instance)
    pg_isready = str(instance.bindir / "pg_isready")
    postgresql_settings = ctx.settings.postgresql
    dsn = db.dsn(instance, postgresql_settings, user=postgresql_settings.surole.name)
    env = postgresql_settings.libpq_environ(
        ctx, instance, postgresql_settings.surole.name
    )
    r = ctx.run([pg_isready, "-d", dsn], env=env)
    if r.returncode == 0:
        return True
    assert r.returncode in (
        1,
        2,
    ), f"Unexpected exit status from pg_isready {r.returncode}: {r.stdout}, {r.stderr}"
    return False


def wait_ready(
    ctx: "Context", instance: "PostgreSQLInstance", *, timeout: int = 10
) -> None:
    for __ in range(timeout):
        if is_ready(ctx, instance):
            return
        time.sleep(1)
    raise exceptions.InstanceStateError(f"{instance} not ready after {timeout}s")


def status(ctx: "Context", instance: "BaseInstance") -> Status:
    """Return the status of an instance."""
    logger.debug("get status of PostgreSQL instance %s", instance)
    return pg_ctl(instance.bindir, ctx=ctx).status(instance.datadir)


def is_running(ctx: "Context", instance: "BaseInstance") -> bool:
    """Return True if the instance is running based on its status."""
    return status(ctx, instance) == Status.running


def check_status(ctx: "Context", instance: "BaseInstance", expected: Status) -> None:
    """Check actual instance status with respected to `expected` one.

    :raises ~exceptions.InstanceStateError: in case the actual status is not expected.
    """
    st = status(ctx, instance)
    if st != expected:
        raise exceptions.InstanceStateError(f"instance is {st.name}")


def show_data_checksums(cnx: db.Connection) -> bool:
    row = cnx.execute("SHOW data_checksums").fetchone()
    assert row is not None
    value = row["data_checksums"]
    assert value in ("on", "off"), value
    return True if value == "on" else False


def get_data_checksums(ctx: "Context", instance: "PostgreSQLInstance") -> bool:
    """Return True/False if data_checksums is enabled/disabled on instance."""
    if is_running(ctx, instance):
        # Use SQL SHOW data_checksums since pg_checksums doesn't work if
        # instance is running.
        with db.connect(ctx, instance) as cnx:
            return show_data_checksums(cnx)
    if instance.version == PostgreSQLVersion.v11:
        command = str(instance.bindir / "pg_verify_checksums")
        proc = ctx.run([command, "--pgdata", str(instance.datadir)])
    else:
        command = str(instance.bindir / "pg_checksums")
        proc = ctx.run([command, "--check", "--pgdata", str(instance.datadir)])
    if proc.returncode == 0:
        return True
    elif proc.returncode == 1:
        return False
    raise exceptions.CommandError(proc.returncode, proc.args, proc.stdout, proc.stderr)


def set_data_checksums(
    ctx: "Context", instance: "PostgreSQLInstance", enabled: bool
) -> None:
    """Enable/disable data checksums on instance."""
    if is_running(ctx, instance):
        raise exceptions.InstanceStateError(
            "could not alter data_checksums on a running instance"
        )
    action = "enable" if enabled else "disable"
    if instance.version < PostgreSQLVersion.v12:
        raise exceptions.UnsupportedError(
            "PostgreSQL <= 11 doesn't have pg_checksums to enable data checksums"
        )
    ctx.run(
        [
            str(instance.bindir / "pg_checksums"),
            f"--{action}",
            "--pgdata",
            str(instance.datadir),
        ],
        check=True,
    )


def replication_lag(
    ctx: "Context", instance: "PostgreSQLInstance"
) -> Optional[Decimal]:
    """Return the replication lag of a standby instance.

    The instance must be running; if the primary is not running, None is
    returned.

    :raises TypeError: if the instance is not a standby.
    """
    standby = instance.standby
    if standby is None:
        raise TypeError(f"{instance} is not a standby")

    try:
        with db.primary_connect(standby) as cnx:
            row = cnx.execute("SELECT pg_current_wal_lsn() AS lsn").fetchone()
    except psycopg.OperationalError as e:
        logger.warning("failed to connect to primary (is it running?): %s", e)
        return None
    assert row is not None
    primary_lsn = row["lsn"]

    password = standby.password.get_secret_value() if standby.password else None
    dsn = db.dsn(
        instance,
        ctx.settings.postgresql,
        dbname="template1",
        user=ctx.settings.postgresql.replrole,
        password=password,
    )
    with db.connect_dsn(dsn) as cnx:
        row = cnx.execute(
            "SELECT %s::pg_lsn - pg_last_wal_replay_lsn() AS lag", (primary_lsn,)
        ).fetchone()
    assert row is not None
    lag = row["lag"]
    assert isinstance(lag, Decimal)
    return lag
