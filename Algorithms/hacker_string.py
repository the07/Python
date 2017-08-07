#!/bin/python3

import sys

def test(input_string):
    test_string = 'hackerrank'
    k = 0
    match = False
    for i in range(0, len(test_string)):
        for j in range(k, len(input_string)):
            if test_string[i] == input_string[j]:
                if i == 9:
                    match = True
                    break
                else:
                    k = j + 1
                    break

    if match:
        return 'YES'
    else:
        return 'NO'


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    result = test(s)
    print (result)
