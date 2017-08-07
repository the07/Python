#!/bin/python3

from time import time
import sys

def migratoryBirds(n, ar):
    # Complete this function
    a = [0] * 5
    for i in ar:
        a[i-1] += 1
    result = a.index(max(a)) + 1
    return result

start_time = time()
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
stop_time = time()

elapsed = stop_time - start_time

print (elapsed)
