import logging
import pathlib
import shutil
import socket
import subprocess
from typing import Any, Callable, Iterator, List, Optional, Set, Tuple
from unittest.mock import MagicMock, patch

import port_for
import pytest
from tenacity import retry
from tenacity.retry import retry_if_exception_type
from tenacity.stop import stop_after_attempt
from tenacity.wait import wait_fixed

from pglift.settings import (
    PostgreSQLVersion,
    SiteSettings,
    _postgresql_bindir_version,
    bindir,
)

default_pg_version: Optional[str]
try:
    default_pg_version = _postgresql_bindir_version()[1]
except EnvironmentError:
    default_pg_version = None


def pytest_addoption(parser: Any) -> None:
    parser.addoption(
        "--pg-version",
        choices=list(PostgreSQLVersion),
        help="Run tests with specified PostgreSQL version (default: %(default)s)",
    )
    parser.addoption(
        "--no-plugins",
        action="store_true",
        default=False,
        help="Run tests without any pglift plugin loaded.",
    )


def pytest_report_header(config: Any) -> List[str]:
    pg_version = config.option.pg_version or default_pg_version
    return [f"postgresql: {pg_version}"]


@pytest.fixture(scope="session")
def no_plugins(request: Any) -> bool:
    value = request.config.option.no_plugins
    assert isinstance(value, bool)
    return value


@pytest.fixture
def datadir() -> pathlib.Path:
    return pathlib.Path(__file__).parent / "data"


@pytest.fixture(scope="session", autouse=True)
def _log_level() -> None:
    logging.getLogger("pglift").setLevel(logging.DEBUG)


@pytest.fixture(scope="session", autouse=True)
def site_config() -> Iterator[Callable[..., Optional[str]]]:
    """Avoid looking up for configuration files in site directories, fall back
    to distribution one.
    """
    from pglift import util

    with patch("pglift.util.site_config", new=util.dist_config) as fn:
        yield fn


@pytest.fixture(autouse=True)
def site_settings() -> Iterator[MagicMock]:
    """Prevent lookup of site settings in XDG user directory or /etc."""
    with patch.object(SiteSettings, "site_settings", return_value=None) as m:
        yield m


@pytest.fixture(scope="session")
def pg_bindir(request: Any) -> Tuple[pathlib.Path, str]:
    version = request.config.option.pg_version or default_pg_version
    if version is None:
        pytest.skip("no PostgreSQL installation found")
    assert isinstance(version, str)
    assert bindir is not None  # otherwise, version would be None too.
    return pathlib.Path(bindir.format(version=version)), version


@pytest.fixture(scope="session")
def pg_version(pg_bindir: Tuple[pathlib.Path, str]) -> str:
    return pg_bindir[1]


@pytest.fixture(scope="session")
def pgbackrest_available(no_plugins: bool) -> bool:
    if no_plugins:
        return False
    return shutil.which("pgbackrest") is not None


@pytest.fixture(scope="session")
def prometheus_execpath(no_plugins: bool) -> Optional[pathlib.Path]:
    if no_plugins:
        return None
    for name in ("prometheus-postgres-exporter", "postgres_exporter"):
        path = shutil.which(name)
        if path is not None:
            return pathlib.Path(path)
    return None


@pytest.fixture(scope="session")
def temboard_execpath(no_plugins: bool) -> Optional[pathlib.Path]:
    if no_plugins:
        return None
    path = shutil.which("temboard-agent")
    if path is not None:
        return pathlib.Path(path)
    return None


@pytest.fixture(scope="session")
def patroni_execpath(no_plugins: bool) -> Optional[pathlib.Path]:
    if no_plugins:
        return None
    path = shutil.which("patroni")
    if path is not None:
        return pathlib.Path(path)
    return None


@pytest.fixture(scope="package")
def tmp_port_factory() -> Iterator[int]:
    """Return a generator producing available and distinct TCP ports."""

    def available_ports() -> Iterator[int]:
        used: Set[int] = set()
        while True:
            port = port_for.select_random(exclude_ports=list(used))
            used.add(port)
            yield port

    return available_ports()


@pytest.fixture(scope="module")
def etcd() -> str:
    p = shutil.which("etcd")
    if p is None:
        pytest.skip("etcd executable not found")
    return p


@pytest.fixture(scope="module")
def etcd_host(
    etcd: str, tmp_path_factory: pytest.TempPathFactory, tmp_port_factory: Iterator[int]
) -> Iterator[str]:
    @retry(
        retry=retry_if_exception_type(ConnectionRefusedError),
        wait=wait_fixed(1),
        stop=stop_after_attempt(5),
    )
    def try_connect(port: int) -> None:
        with socket.socket() as s:
            s.connect(("localhost", port))

    datadir = tmp_path_factory.mktemp("etcd")
    host = "127.0.0.1"
    peer_port = next(tmp_port_factory)
    client_port = next(tmp_port_factory)
    client_url = f"http://{host}:{client_port}"
    cmd = [
        etcd,
        "--data-dir",
        str(datadir),
        "--listen-peer-urls",
        f"http://{host}:{peer_port}",
        "--listen-client-urls",
        client_url,
        "--advertise-client-urls",
        client_url,
    ]
    try:
        proc = subprocess.Popen(cmd)
    except FileNotFoundError as e:
        pytest.skip(f"etcd not available: {e}")
    try_connect(client_port)
    yield f"{host}:{client_port}"
    proc.kill()
