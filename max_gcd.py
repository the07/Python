#!/bin/python3

import sys

def gcd(x,y):
    """ Function to calculate the gcd"""
    result = x % y
    if result == 0:
        return y
    return gcd(y, result)

def maximumGcdAndSum(A, B):
    # Complete this function
    A.sort()
    B.sort()
    i, j = n, n
    max_gcd = 0
    pair_sum = 0
    while i:
        if max_gcd > max(A[i], B[i]):
            return max_gcd
            
    i = 0
    max_gcd = 0
    pair_sum = 0
    while i:
        hcf = gcd(A[i], B[i])
        pair_sum = A[i] + B[i]
        i += 1
        if hcf > max_gcd:
            max_gcd = hcf
            max_pair_sum = pair_sum
        elif hcf == max_gcd and pair_sum > max_pair_sum:
            max_gcd = hcf
    return max_pair_sum

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    res = maximumGcdAndSum(A, B)
    print(res)
