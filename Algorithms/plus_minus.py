n =int(input())

positive = 0
negative = 0
zeroes = 0

for i, x in enumerate(list(map(int, input().strip().split()))):
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zeroes += 1

print (positive/n)
print (negative/n)
print (zeroes/n)
