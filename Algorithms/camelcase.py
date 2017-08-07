#!/bin/python3

import sys

def validate(s):
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

s_len = int(input().strip())
s = input().strip()
max_length = 0
list_of_characters = list(set(s))

for i in range(len(list_of_characters)):
    for j in range(i+1, len(list_of_characters)):
        possible_string = [c for c in s if list_of_characters[i] == c or list_of_characters[j] == c]
        if validate(possible_string) and len(possible_string) > max_length:
            max_length = len(possible_string)

print (max_length)    
