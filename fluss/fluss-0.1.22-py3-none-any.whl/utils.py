from typing import List
from fluss.api.schema import NodeFragment, EdgeFragment, DiagramFragment
from fluss.traits import Edge, Node, Diagram


def find_connected_edges(
    node: NodeFragment, diagram: DiagramFragment
) -> List[EdgeFragment]:
    con_edges = []

    for el in diagram.elements:
        if isinstance(el, Edge):
            if el.source == node.id:
                con_edges.append(el)

    return con_edges
