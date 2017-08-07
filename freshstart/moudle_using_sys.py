from sys import argv, path
from os import getcwd
def print_max(x,y):
    if x > y:
        print('{0} is greater'.format(x))
    elif x == y:
        print('Both are equal')
    else:
        print('{0} is greater'.format(y))

print_max(argv[1],argv[2])

print(path[0])

print(getcwd())
