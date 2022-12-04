from typing import Any


def wrap_in_system_exit(fn: Any) -> None:
    raise SystemExit(fn)
