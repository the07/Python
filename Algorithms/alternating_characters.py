#!/bin/python3

import sys

def alternatingCharacters(s):
    # Complete this function
    s = list(s)
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            s.remove[s[i+1]]
    return s


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
