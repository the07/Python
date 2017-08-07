#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    i = 0
    count = 0
    while (i < (n - m + 1)):
        if sum(s[i:i+m]) == d:
            count += 1
        i += 1
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
