#!/bin/python3

import sys

n = int(input().strip())
s = input().strip()
k = int(input().strip())

def convert(character, k):
    A = ord(character)
    while A + k > 122:
        k = k - (122 - A)
        A = 96
    A = A + k
    return chr(A)

s = list(s)
output = []

for each_item in s:
    if ord(each_item) > 64 and ord(each_item) < 91:
        output.append(convert(each_item.lower(), k).upper())
    elif ord(each_item) > 96 and ord(each_item) < 123:
        output.append(convert(each_item, k))
    else:
        output.append(each_item)

print (''.join(output))
