#!/bin/python3

import sys

def gcd(item):
    result = item[0]
    for i in item[1:]:
        while i % result != 0:
            i, result = result, i % result
    return result

def lcm(item):
    result = item[0]
    for i in item[1:]:
        result = (result * i) // gcd([result, i])
    return result

def getTotalX(a, b):
    # Complete this function
    count = 0
    hcf = gcd(b)
    lcm_a = lcm(a)
    n = 1
    multiple = 1
    while multiple <= hcf:
        multiple = lcm_a * n
        if hcf % multiple == 0:
            count += 1
        n += 1
    return count

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
