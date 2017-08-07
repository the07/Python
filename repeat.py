import re
m = re.findall('(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]',input().strip())
if m:
    print(*m, sep='\n')
else:
    print(-1)
