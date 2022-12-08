import numpy as np

from .shape import Shape


class TriangleSet(Shape):
    def __init__(self, points, faces):
        super().__init__()
        self._points = points
        self._faces = faces

    def __getitem__(self, item):
        return self._points[item]

    def __add__(self, other):
        trs = self.copy()
        nb = len(trs._points)
        trs._points += [np.array(pt) for pt in other.points()]
        trs._faces += [tuple(i + nb for i in inds) for inds in other.faces()]
        return trs

    def points(self):
        """Accessor to the points defining the shape.

        Returns:
            (list)
        """
        return self._points

    def faces(self):
        """Accessor to the faces defining the shape.

        Returns:
            (list)
        """
        return self._faces

    def copy(self):
        """Copy of shape

        Returns:
            (Shape)
        """
        return TriangleSet([np.array(pt) for pt in self._points],
                           [tuple(face) for face in self._faces])

    def apply(self, matrix):
        """Apply transformation.

        Args:
            matrix (np.Array): (4,4) transformation matrix

        Returns:
            None
        """
        points = []
        for pt in self._points:
            vec = np.ones((4,))
            vec[:3] = pt
            vec = matrix.dot(vec)
            points.append(vec[:3])

        self._points = points


def cube():
    """Construct a unit cube centered around origin

    Notes:
      - cube side is equal to 1
      - cube normals are oriented outward

    Returns:
        (TriangleSet)
    """
    pts = [(-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5),
           (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5)]

    faces = [(0, 1, 3), (1, 2, 3),
             (4, 7, 5), (5, 7, 6),
             (0, 3, 4), (7, 4, 3),
             (1, 0, 5), (4, 5, 0),
             (3, 2, 7), (6, 7, 2),
             (1, 5, 2), (6, 2, 5)]

    return TriangleSet([np.array(pt) for pt in pts], faces)
