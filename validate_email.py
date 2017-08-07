import email.utils
import re

N = int(input())

pattern = r'^[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
while N > 0:
    N = N - 1
    S = email.utils.parseaddr(input().strip('\n'))
    print(S)
    if bool(re.match(pattern, S[1])):
        print(email.utils.formataddr(S))
