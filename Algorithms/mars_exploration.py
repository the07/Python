#!/bin/python3

import sys


S = input().strip()
count = 0
expected_input = ['S', 'O', 'S']
for i in range(0, len(S), 3):
    for each_item in expected_input:
        if not each_item == S[i]:
            count += 1
        i += 1

print (count)
