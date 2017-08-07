class Vector:
    """Represent a vector in a multidimensional space"""

    def __init__(self, d):
        """Create d-dimensional vector of zeros"""
        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, list):
            self._coords = [0] * len(d)
            for j in range(len(d)):
                self._coords[j] = d[j]

    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return the jth coordinate of the vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set the jth coordinate of the vector to the given value"""
        self._coords[j] = val

    def __add__(self, other):
        """Return the sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        """Return the difference of the two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, other):
        """Return the product of a vector and a scalar"""
        if isinstance(other, int):
            for j in range(len(self)):
                self[j] *= other
            return self
        elif isinstance(other, Vector) and len(self) == len(other):
            result = 0
            for j in range(len(self)):
                result = self[j] + other[j]
            return result

    def __eq__(self, other):
        """Return true if vector has same coordinates as other"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return true if vector differs from the other"""
        return not self == other #Relies on existing eq

    def __str__(self):
        """Produce string representation of the vector"""
        return '<' + str(self._coords)[1:-1] + '>'

    def __neg__(self):
        """Return a negated vector of itself"""
        for j in range(len(self)):
            self[j] = self[j] * -1
        return self

if __name__ == '__main__':

    vector = Vector([1,2,3])
    print (len(vector))
    print (str(vector))
