from abc import ABCMeta, abstractmethod

class Sequence(meta=ABCMeta):
    """Our version of collections.Sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""

    def __contains__(self, val):
        """Return true if value in sequence, else, False"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return leftmost index at which value is found"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        if len(self) == len(other):
            for j in range(len(self)):
                if not self[j] == other[j]:
                    return False
            return True

if __name__ == '__main__':

    a = Sequence(['Hello'])
