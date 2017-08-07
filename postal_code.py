import re

n = int(input())

print(bool(re.match(r'^[1-9][0-9]{5}$', n) and len(re.findall(r'(?=(\d)\d\1)', n)) <= 1))
