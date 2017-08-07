n, k = map(int, input().split(' '))
c = list(map(int, input().split(' ')))
b = int(input())

b_actual = (sum(c) - c[k])//2

if b_actual == b:
    print ('Bon Apetit')
else:
    print (b - b_actual)

    
