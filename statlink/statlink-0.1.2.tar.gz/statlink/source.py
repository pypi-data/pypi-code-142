from __future__ import annotations

import asyncio
from contextlib import suppress
from typing import List
from urllib.parse import urldefrag

from lxml.etree import ParserError
from lxml.html import document_fromstring

from .utils import URL_RE_MULTI, threaded


class GenericSource:
    def __init__(
        self,
        location: str,
        content: str,
        depth: int = 0,
    ):
        self.location = location
        self.content = content
        self.depth = depth
        self.loop = asyncio.get_running_loop()

    @staticmethod
    def is_valid(url: str) -> bool:
        if not url.startswith("http"):
            return False
        return True

    @threaded
    def find_urls(self) -> List[str]:
        return [
            urldefrag(url)[0]
            for url in URL_RE_MULTI.findall(self.content)
            if self.is_valid(urldefrag(url)[0])
        ]


class FileSource(GenericSource):
    @classmethod
    def from_path(cls, path: str) -> FileSource:
        with open(path) as f:
            return cls(location=path, content=f.read())


class HTMLSource(GenericSource):
    @threaded
    def find_urls(self) -> List[str]:
        with suppress(ValueError, ParserError):
            tree = document_fromstring(self.content)
            tree.make_links_absolute(self.location)
            return [
                urldefrag(url[2])[0]
                for url in tree.iterlinks()
                if self.is_valid(urldefrag(url[2])[0])
            ]
        return []
