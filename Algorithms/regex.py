import re

T = int(input())
pattern = r'^[+-]?[0-9]*\.[0-9]+$'

while T > 0:
    T = T - 1
    S = input()
    print(bool(re.match(pattern, S)))
