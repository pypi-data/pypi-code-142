from __future__ import annotations

from pathlib import Path

import pooch

__all__ = ["get", "Blob"]


def get(hexhash: str) -> Blob:
    if len(hexhash) != 64:
        raise ValueError("hexhash must be 64 characters long")

    url = f"https://pub.danilohorta.me/{hexhash}"
    path = Path(pooch.retrieve(url=url, known_hash=f"sha256:{hexhash}"))
    return Blob(path, hexhash)


class Blob:
    def __init__(self, path: Path, hexhash: str):
        self._path = path.resolve()
        self._hexhash = hexhash

    def as_path(self, name) -> Path:
        path = self._path.parent / name
        if not path.exists():
            path.hardlink_to(self._path)
        return path

    def __str__(self) -> str:
        return self._hexhash
