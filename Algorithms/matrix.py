import re

T = ''.join([''.join(i) for i in list(zip(*[list(input()) for i in range(int(input()[0]))]))])
pattern = r'(?<=\w)\W+(?=\w)'

print(re.sub(pattern, ' ', T))
