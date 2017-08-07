import re

S = input()
k = input()

m = re.finditer(r'(?='+k+')', S)

if re.search(k, S):
    for i in m:
        print((i.start(), i.start()+len(k)-1))
else:
    print((-1, -1))
