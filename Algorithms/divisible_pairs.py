n, k = map(int, input().split())
array = list(map(int, input().strip().split()))
count = 0
for i in range(0,n-1):
    for j in range(i+1, n):
        if (array[i] + array[j]) % k == 0:
            count += 1

print (count)
