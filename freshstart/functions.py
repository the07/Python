def say_hello():
    print ('{0}'.format('hello everyone'))

def print_max(a,b):
    if a > b:
        print('{0} is maximim'.format(a))
    elif a == b:
        print('{0} and {1} are equal'.format(a,b))
    else:
        print('{0} is maximim'.format(b))

def func():
    global x

    print ('x is', x)
    x = 2
    print('Changed global x to', x)

def say(message, times=1):
    print (message * times)

def func1(a, b=5, c=10):
    print('a is {0}, b is {1}, c is {2}'.format(a,b,c))

def total(a=1, *numbers, **phonebook):
     #*number is a tuple, **phonebook is a dictionary
     print ('a', a)

     for item in numbers:
         print(item)

     for key, value in phonebook.items():
         print(key, value)

def maximum(a, b):
    if a > b:
        return a
    elif a ==b :
        return 'The numbers are equal'
    else:
        return b
