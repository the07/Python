import time

def fibonacci(n):
    """Returns the nth fibonacci number"""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    """Fibonacci without recursion"""

    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a, b, end=' ')
        count = 2
        while count != n:
            c = a + b
            print(c, end=' ')
            b, a = c, b
            count += 1

if __name__ == '__main__':

    n = int(input('Enter the value of N:'))
    time1 = time.time()
    for i in range(n):
        print(fibonacci(i), end=" ")
    time2 = time.time()
    diff = time2 - time1
    print('\nTime taken for execution: {} seconds'.format(round(diff,4)))
    time3 = time.time()
    fibonacci2(n)
    time4 = time.time()
    print('\nTime taken for execution: {} seconds'.format(round(time4-time3, 6)))
