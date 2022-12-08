"""
Base description of graph of objects in space
"""
from dataclasses import dataclass, field
from typing import List, Union

from .shape import Shape
from .transfo import Transfo


@dataclass
class ScNode:
    """Node/Graph for shapes in space
    """

    parent: "ScNode" = None
    """Parent of this node in the graph.
    """

    children: List["ScNode"] = field(default_factory=list)
    """Children of this node, transfos are propagated to children.
    """

    shape: Union[Shape, str] = None
    """Actual geometry (or ref to def) for that node.
    """

    transfos: List[Transfo] = field(default_factory=list)
    """Set of transformations associated to this node.
    
    Transfo are applied from first to last.
    """

    meta: dict = field(default_factory=dict)
    """Meta data associated to this node.
    
    Only simple python objects are allowed (for io json)
    """

    def add(self, node):
        """Append children

        Args:
            node (Scene|ScNode): node to add

        Returns:
            None
        """
        self.children.append(node)
        node.parent = self

    def add_transfo(self, transfo):
        """Add new transformation

        Args:
            transfo (Transfo): transfo to append (will be applied last)

        Returns:
            None
        """
        self.transfos.append(transfo)

    def get_shape_inst(self):
        """Return an instance of associated shape.

        Notes: node must be part of a scene in case of ref to shape.

        Returns:
            (Shape): dereferenced (if needed) instance of shape
        """
        if isinstance(self.shape, str):  # def
            sc = self
            while sc.parent is not None:
                sc = sc.parent

            assert isinstance(sc, Scene)
            shp = sc.get_def(self.shape)
        else:
            shp = self.shape

        return shp

    def get_transfo(self, name):
        """Access a transfo by its name.

        Raises: KeyError if no transfo by that name can be found.

        Args:
            name (str): name of transfo (must have been previously defined in transfo)

        Returns:
            (Transfo): ref to first transfo with that name in list of transformations
        """
        for tr in self.transfos:
            try:
                if tr.name == name:
                    return tr
            except AttributeError:
                pass

        raise KeyError(f"no transfo with that name '{name}' in the list")


@dataclass
class Scene(ScNode):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        self._defs = {}

    def add_def(self, obj, oid=None):
        """Store any object in scene as def.

        Raises: KeyError is oid already used

        Args:
            oid (str): id to use to later access this object
            obj (Shape):

        Returns:
            (str): id used to store object
        """
        if oid is None:
            ind = len(self._defs)
            while f"obj_{ind:03d}" in self._defs:
                ind += 1

            oid = f"obj_{ind:03d}"

        self._defs[oid] = obj

        return oid

    def get_def(self, oid):
        """Access stored object.

        Raises: KeyError is oid not used

        Args:
            oid (str): key used to store object

        Returns:
            (Shape)
        """
        return self._defs[oid]

    def merge(self, other, as_node=True):
        """Merge another scene in this one.

        Args:
            other (Scene): other scene to merge (no copy)
            as_node (bool): whether to insert the other scene as single node
                            or to add all children of scene directly

        Returns:
            (None): merge in place
        """
        self._defs.update(other._defs)  # potential risk of duplication, to check?
        if as_node:
            self.add(other)
        else:
            assert len(other.transfos) == 0
            for child in other.children:
                self.add(child)

    def __iadd__(self, other):
        self.merge(other, as_node=False)
        return self
