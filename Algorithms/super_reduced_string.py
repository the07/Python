#!/bin/python3

import sys

class super_string():
    """A super_string class"""

    def __init__(self, item):

        self._string = item

    def __len__(self):

        return len(self._string)

    def pop(self, index):

        if index == 0:
            self._string = self._string[2:]
        else:
            self._string = self._string[:index] + self._string[index+2:]

    def check(self):

        for i in range(0, len(self) - 1):

            if self._string[i] == self._string[i+1]:
                return i
        return -1

    def print_super_string(self):

        return ''.join(self._string)


def super_reduced_string(s):
    # Complete this function
    s = list(s)
    new_string = super_string(s)
    i = new_string.check()
    while i >= 0:
        new_string.pop(i)
        i = new_string.check()
        continue
    return new_string

s = input().strip()
result = super_reduced_string(s)
if len(result) > 0:
    print(result.print_super_string())
else:
    print ('Empty String')
