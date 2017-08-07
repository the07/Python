def factorial(number):
    """ Returns the factorial of a number"""

    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * factorial(number -1)

def permutation(num1, num2):
    """Returns num1Pnum2 = num1!/((num1-num2)!*num2!)"""

    return factorial(num1)//factorial(num1-num2)


n, m, c = map(int, input().split())

##Total unique cities
T = n + m - c
J = n - c
Z = m - c

##L'viv is final and also one of the common cities
T = T - 1
c = c - 1

##Calculate ways to visit the remaining c common cities
Cc = permutation(T, c)

##Update remaining cities once the common cities have been decided
T = T - c

##Calculate ways in which remaining cities can be visited

Cr = (permutation(T, J)*permutation(T-J, Z)) + (permutation(T, Z)*permutation(T-Z, J))

print ((Cc * Cr)//2)
