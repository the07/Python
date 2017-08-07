#!/bin/python3

from time import time
import sys

def binary_search(data, target, low, high):

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

if __name__ == '__main__':

    print ('Enter a sequence of numbers\n')
    data = list(map(int, input().split(' ')))
    print ('Enter the number you are searching for: ')
    target = int(input())
    low = 0
    high = len(data) - 1
    start_time = time()
    print (binary_search(data, target, low, high))
    end_time = time()
    elapsed_time = start_time - end_time
    print (elapsed_time)
