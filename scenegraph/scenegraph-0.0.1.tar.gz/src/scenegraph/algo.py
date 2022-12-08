"""
Simple algo on scenegraph
"""
import numpy as np


def get_meta(node, name, default=None):
    """Get meta property associated to node.

    This function will explore ancestors to find the first defined meta
    if necessary.

    Args:
        node (ScNode): node to consider
        name (str): name of property
        default (any): in case no meta is defined for any parent

    Returns:
        (any)
    """
    try:
        return node.meta[name]
    except KeyError:
        if node.parent is None:
            return default
        else:
            return get_meta(node.parent, name, default)


def transfo_tot(node, absolute=False):
    """Concatenate all transfo for this node.

    Args:
        node (ScNode): node to consider
        absolute (bool): whether transfo use ancestors

    Returns:
        (np.array)
    """
    tr_loc = np.identity(4)
    for transfo in node.transfos:
        tr_loc = transfo.matrix() @ tr_loc

    if absolute and node.parent is not None:
        tr_parent = transfo_tot(node.parent, absolute)
        tr_loc = tr_parent @ tr_loc

    return tr_loc


def _points(node, tr_parent, pts):
    """Absolute position of points of all descendant of node

    Args:
        node (ScNode):
        tr_parent (Transfo): transformation of parent
        pts (list): where to store computed points

    Returns:
        (None): modify pts in place
    """
    tr_loc = np.identity(4)
    for transfo in node.transfos:
        tr_loc = transfo.matrix() @ tr_loc

    tr_loc = tr_parent @ tr_loc
    if node.shape is not None:
        mesh = node.get_shape_inst().copy()
        mesh.apply(tr_loc)
        pts.extend(mesh.points())

    for child in node.children:
        _points(child, tr_loc, pts)


def bounding_box(node, tr_parent=None):
    """Bounding box of node and all its descendants.

    Args:
        node (ScNode):
        tr_parent (Transfo): transformation of parent, if None will use identity

    Returns:
        (np.array, np.array): (xmin, ymin, zmin), (xmax, ymax, zmax)
    """
    if tr_parent is None:
        tr_parent = np.identity(4)

    pts = []
    _points(node, tr_parent, pts)

    pts = np.array(pts)
    return pts.min(axis=0, initial=np.inf), pts.max(axis=0, initial=-np.inf)
