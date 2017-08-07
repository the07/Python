s = str(input())
n = int(input())

count = s.count('a')

count = count*(n//len(s)) + (s[:n%len(s)]).count('a')

print(count)
