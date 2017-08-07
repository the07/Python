S = input()

print(*sorted(S, key = lambda x: (x in '02468', x.isdigit(), x.isupper(), x)), sep='')
