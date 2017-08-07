def is_subset(A, B):
    for i in range(len(A)):
        if (A[i] == '0' and B[i] == '1'):
            return False
    return True

n, m = map(int, input().strip().split())
D= {}
while m > 0:
    *arg, testset = input().strip().split()
    if len(arg) == 2:
        D[testset] = arg
    if len(arg) == 1:
        value = 0
        for item in D:
            if is_subset(item, testset):
                print (item, testset)
                if D[item][0] == '1':
                    value = D[item][1]
                elif D[item][0] == '2':
                    value = int(value) ^ int(D[item][1])
        print (value)
    m = m - 1
