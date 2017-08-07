from decimal import getcontext, Decimal

def calculate_pi(precision):
    """Return the value of pi using Bailey-Browein-Plouffe algorithm"""

    getcontext().prec = precision
    formula = sum(1 / Decimal(16) ** k * (Decimal(4) / Decimal(8 * k + 1) -
                                          Decimal(2) / Decimal(8 * k + 4) -
                                          Decimal(1) / Decimal(8 * k + 5) -
                                          Decimal(1) / Decimal(8 * k + 6))
                                          for k in range(precision))
    return formula

if __name__ == '__main__':

    precision = int(input('Enter the number of decimal places:'))
    answer = calculate_pi(precision + 1)

    i = 0

    print(answer)
