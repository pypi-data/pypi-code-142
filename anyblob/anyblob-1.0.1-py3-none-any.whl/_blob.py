from __future__ import annotations

import hashlib
from pathlib import Path

import pooch

__all__ = ["get", "Blob"]

BUFSIZE = 4 * 1024 * 1024


def hash_file(path: Path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while data := f.read(BUFSIZE):
            h.update(data)
    return h.hexdigest()


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

        if path.exists() and hash_file(path) != self._hexhash:
            path.unlink()

        if not path.exists():
            path.hardlink_to(self._path)

        return path

    def __str__(self) -> str:
        return self._hexhash
