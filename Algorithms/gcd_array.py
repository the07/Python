#!/bin/python3
#Python program to find the GCD of an array of numbers

def gcd(a):
    result = a[0]
    for i in a[1:]:
        while i % result != 0:
            i, result = result, i % result
    return result

arr = list(map(int, input().split()))
h = gcd(arr)

print (h)
