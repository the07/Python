import re

for _ in range(int(input())):
    n = input().strip()

    if len(n) not in (16, 19) or n[0] not in ('4','5','6'):
        print('Invalid')
        continue
    if len(n) == 19:
        if re.match(r'\d{4}-\d{4}-\d{4}-\d{4}',n):
            n = n.replace('-', '')
        else:
            print('Invalid')
            continue
    if not n.isnumeric() or re.search(r'(\d)\1{3,}', n):
        print('Invalid')
        continue
    print('Valid')                
