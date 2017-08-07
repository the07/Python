#!/bin/python3

import sys

def super_reduced_string(s):
    # Complete this function
    i = 1
    while i > 0:
        if (len(s) < 2) or (i == len(s)):
            return s
        if s[i] == s[i-1]:
            s = s[0:i-1] + s[i+1:]
            i = 1
        else:
            i += 1
    return s

s = input().strip()
result = super_reduced_string(s)
if len(result) > 0:
    print(result)
else:
    print ('Empty String')
