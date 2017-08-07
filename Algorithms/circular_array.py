n, k, q = map(int, input().split())
array = list(map(int, input().strip().split()))

while k:
    t = array.pop()
    array.insert(0, t)
    k = k - 1

while q:
    m = int(input())
    print(array[m])
    q = q - 1
