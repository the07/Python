n = int(input())

arr = list(map(int, input().strip().split()))
while len(arr) > 0:
    print (len(arr))
    t = min(arr)
    arr = [item - t for item in arr if item > t]
