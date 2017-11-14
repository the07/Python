#!/bin/python3

import sys

def binary_search(data, target, low, high):
    """ Return true if target is found"""

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)

        else:
            return binary_search(data, target, mid+1, high)

data = list(map(int, input().split(' ')))

target = int(input().strip())

low = 0
high = len(data) - 1

if binary_search(data, target, low, high):
    print ('Found')
else:
    print ('Not founda')
