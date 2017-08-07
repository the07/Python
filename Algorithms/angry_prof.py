T = int(input())

while T:
    n, k = map(int, input().split())
    array = list(map(int, input().strip().split()))
    count = 0
    for i, x in enumerate(array):
        if x <= 0:
            count += 1
    if count < k:
        print ('YES')
    else:
        print ('NO')
    T = T - 1
