from __future__ import annotations

from typing import List, Optional

from .request import Request, RequestState
from .utils import truncate_url


class Node:
    def __init__(
        self,
        location: str,
        request: Optional[Request],
    ):
        self.location = location
        self.request = request
        self.links: List[Node] = []

    def count_links_total(self) -> int:
        return len(self.links)

    def count_links_ok(self) -> int:
        return len([link for link in self.links if link.request and link.request.ok()])

    def links_all_completed(self) -> bool:
        return all(
            [
                link.request.state is RequestState.COMPLETED
                for link in self.links
                if link.request
            ]
        )

    def count_links_completed(self):
        return len(
            [
                link
                for link in self.links
                if link.request and link.request.state is RequestState.COMPLETED
            ]
        )

    def count_in_progress(self) -> int:
        return len(
            [
                link
                for link in self.links
                if link.request and link.request.state is RequestState.IN_PROGRESS
            ]
        )

    def get_result_string(self) -> str:
        return (
            f"{truncate_url(self.location, 79, '...')} "
            f"[{self.count_links_ok()}/{self.count_links_total()}] "
        )
