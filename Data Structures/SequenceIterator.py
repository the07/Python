class SequenceIterator:
    """An iterator for any of Python's sequence types"""

    def __iter__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """Return the next element or raise the StopIteration error"""
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
