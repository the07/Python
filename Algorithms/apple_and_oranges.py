#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

count_apple = 0
count_orange = 0

for each_apple in apple:
    if (a+each_apple) >= s and (a+each_apple) <= t:
        count_apple += 1

for each_orange in orange:
    if (b+each_orange) <= t and (b+each_orange) >= s:
        count_orange += 1

print (count_apple)
print (count_orange)
