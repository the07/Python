T = str(input())

suffix = T[-2:]
arg = T[:-2].split(':')
if suffix == 'AM':
    arg[0] = int(arg[0]) % 12
    arg[0] = str(arg[0]).zfill(2)
else:
    arg[0] = 12 + (int(arg[0]) % 12)
    arg[0] = str(arg[0]).zfill(2)

print (':'.join(arg))
