#!/bin/python3

import sys


n = int(input().strip())
A = [list(map(int, input().strip().split())) for _ in range(n)]
sum_left = 0
sum_right = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum_left += A[i][j]
        if j == n-1-i:
            sum_right += A[i][j]

print (abs(sum_left - sum_right))
