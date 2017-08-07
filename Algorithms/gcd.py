#!/bin/python3
#Python program to calculate the gcd of 2 numbers

def gcd(x,y):
    result = x % y
    if result == 0:
        return y
    return gcd(y,result)

print ('Enter two numbers to calculate the GCD')
x,y = map(int, input().split(' '))

hcf = gcd(x,y)
print (hcf)
