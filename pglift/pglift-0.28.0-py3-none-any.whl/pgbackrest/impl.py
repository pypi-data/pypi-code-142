import configparser
import datetime
import json
import os
import re
from functools import partial
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Iterator,
    List,
    Literal,
    Optional,
    Union,
    overload,
)

from dateutil.tz import gettz
from pgtoolkit import conf as pgconf

from .. import exceptions, postgresql, util
from ..models import interface
from ..task import task
from ..types import BackupType
from .models import Service

if TYPE_CHECKING:
    from ..ctx import Context
    from ..models import system
    from ..settings import PgBackRestSettings, Settings


def available(settings: "Settings") -> Optional["PgBackRestSettings"]:
    return settings.pgbackrest


def get_settings(settings: "Settings") -> "PgBackRestSettings":
    """Return settings for pgbackrest

    Same as `available` but assert that settings are not None.
    Should be used in a context where settings for the plugin are surely
    set (for example in hookimpl).
    """
    assert settings.pgbackrest is not None
    return settings.pgbackrest


def enabled(
    instance: "system.PostgreSQLInstance", settings: "PgBackRestSettings"
) -> bool:
    return system_lookup(instance.datadir, settings) is not None


def base_config(settings: "PgBackRestSettings") -> Path:
    return settings.configpath / "pgbackrest.conf"


def config_directory(settings: "PgBackRestSettings") -> Path:
    return settings.configpath / "conf.d"


def make_cmd(stanza: str, settings: "PgBackRestSettings", *args: str) -> List[str]:
    return [
        str(settings.execpath),
        f"--config-path={settings.configpath}",
        f"--stanza={stanza}",
    ] + list(args)


parser = partial(configparser.ConfigParser, strict=True)

pgpath_rgx = re.compile(r"pg(\d+)-path")


def system_lookup(datadir: Path, settings: "PgBackRestSettings") -> Optional[Service]:
    d = config_directory(settings)
    for p in d.glob("*.conf"):
        cp = parser()
        with p.open() as f:
            cp.read_file(f)
        for stanza in cp.sections():
            for key, value in cp.items(stanza):
                m = pgpath_rgx.match(key)
                if m and value == str(datadir):
                    return Service(stanza=stanza, path=p, index=int(m.group(1)))
    return None


@overload
def backup_info(
    ctx: "Context",
    service: Service,
    settings: "PgBackRestSettings",
    *,
    backup_set: Optional[str] = None,
    output_json: Literal[False],
) -> str:
    ...


@overload
def backup_info(
    ctx: "Context",
    service: Service,
    settings: "PgBackRestSettings",
    *,
    backup_set: Optional[str] = None,
) -> Dict[str, Any]:
    ...


def backup_info(
    ctx: "Context",
    service: Service,
    settings: "PgBackRestSettings",
    *,
    backup_set: Optional[str] = None,
    output_json: bool = True,
) -> Union[Dict[str, Any], str]:
    """Call pgbackrest info command to obtain information about backups.

    Ref.: https://pgbackrest.org/command.html#command-info
    """
    args = []
    if backup_set is not None:
        args.append(f"--set={backup_set}")
    if output_json:
        args.append("--output=json")
    args.append("info")
    r = ctx.run(make_cmd(service.stanza, settings, *args), check=True)
    if not output_json:
        return r.stdout
    infos = json.loads(r.stdout)
    try:
        return next(i for i in infos if i["name"] == service.stanza)  # type: ignore[no-any-return]
    except StopIteration:
        return {}


@task("setting up pgBackRest")
def setup(
    ctx: "Context",
    service: Service,
    settings: "PgBackRestSettings",
    instance_config: pgconf.Configuration,
    datadir: Path,
) -> None:
    """Setup pgBackRest"""
    base_config_path = base_config(settings)
    if not base_config_path.exists():
        raise exceptions.SystemError(
            f"Missing base config file {base_config_path} for pgbackrest. "
            "Did you forget to run 'pglift site-configure'?"
        )
    stanza = service.stanza
    stanza_confpath = service.path
    pg = f"pg{service.index}"
    cp = parser()
    if stanza_confpath.exists():
        with stanza_confpath.open() as f:
            cp.read_file(f)

    # Always use string values so that this would match with actual config (on
    # disk) that's parsed later on.
    config = {
        stanza: {
            f"{pg}-path": str(datadir),
            f"{pg}-port": str(instance_config.get("port", 5432)),
            f"{pg}-user": ctx.settings.postgresql.backuprole.name,
        },
    }
    unix_socket_directories = instance_config.get("unix_socket_directories")
    if unix_socket_directories:
        config[stanza][f"{pg}-socket-path"] = str(
            instance_config.unix_socket_directories
        )
    cp.read_dict(config)
    with stanza_confpath.open("w") as configfile:
        cp.write(configfile)


@task("upgrading pgBackRest stanza {service.stanza}")
def upgrade(
    ctx: "Context",
    instance: "system.PostgreSQLInstance",
    service: Service,
    settings: "PgBackRestSettings",
    password: Optional[str],
) -> None:
    """Upgrade stanza"""
    stanza = service.stanza
    ctx.run(make_cmd(stanza, settings, "stanza-upgrade", "--no-online"), check=True)
    if postgresql.is_running(ctx, instance):
        check(ctx, instance, service, settings, password)


def postgresql_configuration(
    stanza: str, settings: "PgBackRestSettings"
) -> pgconf.Configuration:
    pgconfig = util.template("postgresql", "pgbackrest.conf").format(
        execpath=settings.execpath, configpath=settings.configpath, stanza=stanza
    )
    config = pgconf.Configuration()
    list(config.parse(pgconfig.splitlines()))
    return config


@setup.revert("deconfiguring pgBackRest")
def revert_setup(
    ctx: "Context",
    service: Service,
    settings: "PgBackRestSettings",
    instance_config: pgconf.Configuration,
    datadir: Path,
) -> None:
    """Un-setup pgBackRest.

    Remove options from 'stanza' section referencing instance's datadir, then
    possibly remove the configuration file if empty, and finally remove
    stanza's log files.
    """
    stanza = service.stanza
    stanza_confpath = service.path
    if stanza_confpath.exists():
        cp = parser()
        with stanza_confpath.open() as f:
            cp.read_file(f)
        for opt in cp.options(stanza):
            if opt.startswith(f"pg{service.index}-"):
                cp.remove_option(stanza, opt)
        with stanza_confpath.open("w") as f:
            cp.write(f)
        if not cp.options(stanza):
            stanza_confpath.unlink(missing_ok=True)
    if not stanza_confpath.exists():
        for logf in settings.logpath.glob(f"{stanza}-*.log"):
            logf.unlink(missing_ok=True)


@task("creating pgBackRest stanza for {instance}")
def init(
    ctx: "Context",
    instance: "system.PostgreSQLInstance",
    service: Service,
    settings: "PgBackRestSettings",
    password: Optional[str],
    *,
    run_check: bool = False,
) -> None:
    ctx.run(
        make_cmd(service.stanza, settings, "stanza-create", "--no-online"), check=True
    )
    if run_check and postgresql.is_running(ctx, instance):
        check(ctx, instance, service, settings, password)


def check(
    ctx: "Context",
    instance: "system.PostgreSQLInstance",
    service: Service,
    settings: "PgBackRestSettings",
    password: Optional[str],
) -> None:
    env = os.environ.copy()
    if password is not None:
        env["PGPASSWORD"] = password
    env = ctx.settings.postgresql.libpq_environ(
        ctx, instance, ctx.settings.postgresql.backuprole.name, base=env
    )
    ctx.run(make_cmd(service.stanza, settings, "check"), check=True, env=env)


@init.revert("deleting pgBackRest stanza for {instance}")
def revert_init(
    ctx: "Context",
    instance: "system.PostgreSQLInstance",
    service: Service,
    settings: "PgBackRestSettings",
    *args: Any,
    **kwargs: Any,
) -> None:
    stanza = service.stanza
    ctx.run(make_cmd(stanza, settings, "stop"), check=True)
    ctx.run(make_cmd(stanza, settings, "stanza-delete", "--force"), check=True)


def backup_command(
    instance: "system.Instance",
    settings: "PgBackRestSettings",
    *,
    type: BackupType = BackupType.default(),
    start_fast: bool = True,
) -> List[str]:
    """Return the full pgbackrest command to perform a backup for ``instance``.

    :param type: backup type (one of 'full', 'incr', 'diff').

    Ref.: https://pgbackrest.org/command.html#command-backup
    """
    args = [
        f"--type={type.name}",
        "--log-level-console=info",
        "backup",
    ]
    if start_fast:
        args.insert(-1, "--start-fast")
    s = instance.service(Service)
    return make_cmd(s.stanza, settings, *args)


@task("backing up instance with pgBackRest")
def backup(
    ctx: "Context",
    instance: "system.Instance",
    settings: "PgBackRestSettings",
    *,
    type: BackupType = BackupType.default(),
) -> None:
    """Perform a backup of ``instance``.

    :param type: backup type (one of 'full', 'incr', 'diff').

    Ref.: https://pgbackrest.org/command.html#command-backup
    """
    if instance.standby:
        raise exceptions.InstanceStateError("backup should be done on primary instance")

    ctx.run(
        backup_command(instance, settings, type=type),
        check=True,
        env=ctx.settings.postgresql.libpq_environ(
            ctx, instance, ctx.settings.postgresql.backuprole.name
        ),
    )


def expire_command(
    instance: "system.Instance", settings: "PgBackRestSettings"
) -> List[str]:
    """Return the full pgbackrest command to expire backups for ``instance``.

    Ref.: https://pgbackrest.org/command.html#command-expire
    """
    s = instance.service(Service)
    return make_cmd(s.stanza, settings, "--log-level-console=info", "expire")


@task("expiring pgBackRest backups")
def expire(
    ctx: "Context", instance: "system.Instance", settings: "PgBackRestSettings"
) -> None:
    """Expire a backup of ``instance``.

    Ref.: https://pgbackrest.org/command.html#command-expire
    """
    ctx.run(expire_command(instance, settings), check=True)


def _parse_backup_databases(info: str) -> List[str]:
    """Parse output of pgbackrest info --set=<label> and return the list of
    databases.

    This is only required until "pgbackrest info" accepts options --set and
    --output=json together.

    >>> set_info = '''stanza: 13-main
    ... status: ok
    ... cipher: none
    ...
    ... db (current)
    ...     wal archive min/max (13-1): 000000010000000000000001/000000010000000000000004
    ...
    ...     full backup: 20210121-153336F
    ...         timestamp start/stop: 2021-01-21 15:33:36 / 2021-01-21 15:33:59
    ...         wal start/stop: 000000010000000000000004 / 000000010000000000000004
    ...         database size: 39.6MB, backup size: 39.6MB
    ...         repository size: 4.9MB, repository backup size: 4.9MB
    ...         database list: bar (16434), foo (16401), postgres (14174)
    ...         symlinks:
    ...             pg_wal => /var/lib/pgsql/13/main/pg_wal_mnt/pg_wal
    ... '''
    >>> _parse_backup_databases(set_info)
    ['bar', 'foo', 'postgres']
    """
    dbs_pattern = re.compile(r"^\s*database list:\s*(.*)$")
    db_pattern = re.compile(r"(\S+)\s*\(.*")
    for line in info.splitlines():
        m = dbs_pattern.match(line)
        if m:
            return [
                re.sub(db_pattern, r"\g<1>", db.strip()) for db in m.group(1).split(",")
            ]
    return []


def iter_backups(
    ctx: "Context", instance: "system.Instance", settings: "PgBackRestSettings"
) -> Iterator[interface.InstanceBackup]:
    """Yield information about backups on an instance."""
    service = instance.service(Service)
    backups = backup_info(ctx, service, settings)["backup"]

    def started_at(entry: Any) -> float:
        return entry["timestamp"]["start"]  # type: ignore[no-any-return]

    for backup in sorted(backups, key=started_at, reverse=True):
        info_set = backup_info(
            ctx,
            service,
            settings,
            backup_set=backup["label"],
            output_json=False,
        )
        databases = _parse_backup_databases(info_set)
        dtstart = datetime.datetime.fromtimestamp(backup["timestamp"]["start"])
        dtstop = datetime.datetime.fromtimestamp(backup["timestamp"]["stop"])
        yield interface.InstanceBackup(
            label=backup["label"],
            size=backup["info"]["size"],
            repo_size=backup["info"]["repository"]["size"],
            date_start=dtstart.replace(tzinfo=gettz()),
            date_stop=dtstop.replace(tzinfo=gettz()),
            type=backup["type"],
            databases=databases,
        )


def restore_command(
    instance: "system.Instance",
    settings: "PgBackRestSettings",
    *,
    date: Optional[datetime.datetime] = None,
    backup_set: Optional[str] = None,
) -> List[str]:
    """Return the pgbackrest restore for ``instance``.

    Ref.: https://pgbackrest.org/command.html#command-restore
    """
    args = [
        "--log-level-console=info",
        # The delta option allows pgBackRest to handle instance data/wal
        # directories itself, without the need to clean them up beforehand.
        "--delta",
        "--link-all",
    ]
    if date is not None and backup_set is not None:
        raise exceptions.UnsupportedError(
            "date and backup_set are not expected to be both specified"
        )
    elif date is not None:
        target = date.strftime("%Y-%m-%d %H:%M:%S.%f%z")
        args += ["--target-action=promote", "--type=time", f"--target={target}"]
    elif backup_set is not None:
        args += ["--target-action=promote", "--type=immediate", f"--set={backup_set}"]
    args.append("restore")
    s = instance.service(Service)
    return make_cmd(s.stanza, settings, *args)


@task("restoring instance with pgBackRest")
def restore(
    ctx: "Context",
    instance: "system.Instance",
    settings: "PgBackRestSettings",
    *,
    label: Optional[str] = None,
    date: Optional[datetime.datetime] = None,
) -> None:
    """Restore an instance, possibly only including specified databases.

    The instance must not be running.

    Ref.: https://pgbackrest.org/command.html#command-restore
    """
    if instance.standby:
        raise exceptions.InstanceReadOnlyError(instance)

    cmd = restore_command(instance, settings, date=date, backup_set=label)
    ctx.run(cmd, check=True)


def env_for(service: "Service", settings: "PgBackRestSettings") -> Dict[str, str]:
    return {
        "PGBACKREST_CONFIG_PATH": str(settings.configpath),
        "PGBACKREST_STANZA": service.stanza,
    }
