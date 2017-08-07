class Progression:
    """Iterator producing a general iterator.

    Default iterator produces the whole number 0, 1, 2...
    """

    def __init__(self, start=0):
        """Initialise current to the start value of the iterator"""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        If None, it represents end of Progression
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or raise StopIteration"""
        if self._current == None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention an iterator must return itself"""
        return self

    def print_progression(self, n):
        """Print next n values of progression"""
        print (' '.join(str(next(self)) for j in range(n)))


class ArithmaticProgression(Progression):
    """Iterator producing an arithmatic progression"""

    def __init__(self, start=0, increment=1):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

class GeometricProgression(Progression):
    """An iterator producing a geometric progression"""

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

class FibonacciProgression(Progression):
    """An iterator producing a Fibonacci Progression"""

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':

    seq = FibonacciProgression(2,2)
    print (seq.print_progression(8))
