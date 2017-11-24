from datetime import datetime

def bad_fibonacci(n):
    """ Return the nth fibonacci number """

    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)


def good_fibonacci(n):
    """ Return the nth fibonacci number. Just one recursion call """

    if n <= 1:
        return (0,n)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b, a)

time_start = datetime.now()
bad_fibonacci(1000)
time_end = datetime.now()

print ("Bad Fibonacci timing: {}".format(time_end - time_start))

time_start = datetime.now()
good_fibonacci(1000)
time_end = datetime.now()

print ("good_fibonacci timing: {}".format(time_end - time_start))
