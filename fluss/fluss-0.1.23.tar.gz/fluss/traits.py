import yaml


class Node:
    id: str

    def connected_nodes(diagram):
        pass

    def to_input(self):
        from fluss.api.schema import NodeInput

        return NodeInput(**self.dict())


class Edge:
    def connected_nodes(diagram):
        pass


class Flow:
    def find_connected_nodes_on():
        pass


class Graph:
    def connected_edges(self, node):
        edges = []
        for el in self.edges:
            if el.source == node.id:
                edges.append(el)

        return edges

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as f:
            g = yaml.safe_load(f)

        return cls(**g)
