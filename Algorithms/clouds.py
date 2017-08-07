n = int(input())

arr = list(map(int, input().strip().split()))
curr = 0
count = 0

while curr is not n - 1:
    if curr + 2 < n and arr[curr+2] == 0:
        curr = curr + 2
        count += 1
    else:
        curr = curr + 1
        count += 1

print (count)
