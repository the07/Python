
global prime
prime = []
def primefactors(n):

    while n % 2 == 0:
        prime.append(2)
        n = n / 2

    for i in range(3, int(n / 2) + 1, 2):
        while n % i == 0:
                prime.append(i)
                n = n / i

if __name__ == "__main__":

    n = int(input('Enter the Number: '))
    primefactors(n)
    print(prime)
