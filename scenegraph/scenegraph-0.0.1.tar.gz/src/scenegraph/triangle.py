"""
Basic triangle primitive
"""
import numpy as np

from .shape import Shape


class Triangle(Shape):
    """Simple triangle in 3D space
    """

    def __init__(self, p0, p1, p2):
        """Constructor

        Args:
            p0 (np.array): 3D point in space
            p1 (np.array): 3D point in space
            p2 (np.array): 3D point in space
        """
        super().__init__()

        self._corners = [p0, p1, p2]

    def __getitem__(self, item):
        return self._corners[item]

    def points(self):
        """Accessor to the three corners of triangle.

        Returns:
            (list)
        """
        return self._corners

    def copy(self):
        """Copy of triangle

        Returns:
            (Triangle)
        """
        return Triangle(*[np.array(pt) for pt in self._corners])

    def apply(self, matrix):
        """Apply transformation.

        Args:
            matrix (np.Array): (4,4) transformation matrix

        Returns:
            None
        """
        corners = []
        for pt in self._corners:
            vec = np.ones((4,))
            vec[:3] = pt
            vec = matrix.dot(vec)
            corners.append(vec[:3])

        self._corners = corners
