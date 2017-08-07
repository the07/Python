import re

T = int(input())

while T > 0:
    try:
        T = T - 1
        S = input()
        re.compile(S)
        is_valid = True
    except re.error:
        is_valid = False

    print(is_valid)
