from decimal import Decimal, getcontext

def factorial(number):
    """ Returns the factorial of a number"""

    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * factorial(number -1)

def calculate_e(precision):
    """Calculates the value of e to the given precision"""

    getcontext().prec = precision
    e = (sum(Decimal(4 * k + 3) / (Decimal(2 ** (2 * k + 1)) * factorial(Decimal(2 * k + 1))) for k in range(100))) ** 2
    return e

if __name__ == '__main__':

    precision = int(input('Enter the precision'))
    e = calculate_e(precision + 1)
    print(e)
