def fibonacci(n):
    """Fibonacci without recursion"""
    global list_fib
    list_fib = []
    a = 0
    b = 1
    if n == 0:
        return list_fib
    elif n == 1:
        list_fib.append(a)
    elif n == 2:
        list_fib.append(a)
        list_fib.append(b)
    else:
        list_fib.append(a)
        list_fib.append(b)
        count = 2
        while count != n:
            c = a + b
            list_fib.append(c)
            b, a = c, b
            count += 1

    return list_fib

N = int(input())

print(list(map(lambda x: x ** 3, fibonacci(N))))
