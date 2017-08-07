import re

pattern = r'^[7-9][0-9]{9,9}$'

N = int(input())

while N > 0:
    N = N - 1
    S = input()
    if bool(re.match(pattern, S)):
        print('YES')
    else:
        print('NO')
