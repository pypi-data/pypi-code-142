import asyncio
import re
from functools import partial, wraps
from pathlib import Path
from typing import Any, Awaitable, Callable, List, TypeVar


T = TypeVar("T")

URL_RE = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"  # noqa
URL_RE_SINGLE = re.compile(f"^{URL_RE}$")
URL_RE_MULTI = re.compile(URL_RE)


def is_url(value: str) -> bool:
    return bool(URL_RE_SINGLE.match(value))


def truncate_url(url: str, max_length: int, placeholder: str) -> str:
    if len(url) > max_length:
        url = url[: max_length - len(placeholder)] + placeholder
    return url


def get_files_path(path: str, recursive: bool = False) -> List[str]:
    root_path = Path(path).resolve()
    files_path, glob = [], ""
    while not root_path.exists():
        root_path, glob = (
            root_path.parent,
            (Path(root_path.name) / glob).as_posix(),
        )

    if root_path.is_dir():
        for file_path in root_path.glob(glob or ("**/*" if recursive else "*")):
            if file_path.is_file():
                files_path.append(file_path)
    elif root_path.is_file():
        files_path.append(root_path)

    return [file_path.as_posix() for file_path in files_path]


def threaded(func: Callable[..., T]) -> Callable[..., Awaitable[T]]:
    @wraps(func)
    def _wrapped(*args: Any, **kwargs: Any) -> Any:
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(None, partial(func, *args, **kwargs))

    return _wrapped
