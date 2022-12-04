from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List
from urllib.parse import urlparse


class URLFilter(ABC):
    @abstractmethod
    def validate(self, url: str) -> bool:
        pass

    def apply(self, urls: List[str]) -> List[str]:
        return [url for url in urls if self.validate(url)]


class OrFilter(List[URLFilter], URLFilter):
    def validate(self, url: str) -> bool:
        return not self or any(url_filter.validate(url) for url_filter in self)


class DomainFilter(URLFilter):
    def __init__(self, domain: str):
        if domain.startswith("www."):
            domain = domain[4:]
        self.domain = domain

    def validate(self, url: str) -> bool:
        return urlparse(url).netloc in [self.domain, f"www.{self.domain}"]

    @classmethod
    def from_url(cls, url: str) -> DomainFilter:
        return cls(domain=urlparse(url).netloc)
