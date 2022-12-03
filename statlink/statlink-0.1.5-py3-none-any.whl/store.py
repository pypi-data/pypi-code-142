from typing import Dict, List, Optional

from .node import Node
from .request import Request, RequestState


class Store:
    def __init__(self):
        self._requests: Dict[str, Request] = {}
        self._graph: Dict[str, Node] = {}

    def add_request(self, request: Request) -> None:
        self._requests[request.url] = request

    def create_or_get_node(self, location: str) -> Node:
        node = self._graph.get(location)
        if not node:
            node = Node(location=location, request=self._requests.get(location))
            self._graph[location] = node
        return node

    def add_edge(self, location_a: str, location_b: str) -> None:
        node_a = self.create_or_get_node(location_a)
        node_b = self.create_or_get_node(location_b)
        node_a.links.append(node_b)

    def get_request(self, url: str) -> Optional[Request]:
        return self._requests.get(url)

    def get_requests_error(self) -> List[Request]:
        return [
            request
            for request in self._requests.values()
            if request.state is RequestState.COMPLETED and not request.ok()
        ]

    def get_requests_completed(self) -> List[Request]:
        return [
            request
            for request in self._requests.values()
            if request.state is RequestState.COMPLETED
        ]

    def get_nodes_processed(self) -> List[Node]:
        return [node for node in self._graph.values() if node.links_all_completed()]
