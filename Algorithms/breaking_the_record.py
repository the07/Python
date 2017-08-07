#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    highest_score = s[0]
    lowest_score = s[0]
    count_high = 0
    count_low = 0
    for i in s[1:]:
        if highest_score < i:
            count_high += 1
            highest_score = i
        elif lowest_score > i:
            count_low += 1
            lowest_score = i
    return [count_high, count_low]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
