class HyperSpace():
    """A hyperspace is n-dimensional space."""

    def __init__(self, n):
        """Initialise the dimension of the space"""

        self._dimesnion = n

    def point(self, ):
        """Represents a point in a n dimensional space.

        For example, point P in 3 dimensional space, P = {x0, x1, x2}.
        Where x0, x1, x2 are coordinates.
        """
