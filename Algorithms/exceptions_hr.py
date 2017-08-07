T = int(input())

while T > 0:
    try:
        T = T - 1
        a,b = input().strip().split()
        c = int(a) // int(b)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
        continue
    except ValueError as v:
        print('Error Code:', v)
        continue
    else:
        print(c)
