n = int(input())

number_of_items = 3
i = 1
found = False

while not found:
    if n in range(i, i+number_of_items):
        found = True
    else:
        i = i + number_of_items
        number_of_items = number_of_items * 2

##the sum of time + value in each stack is equal. ex. in first stack it is 4, in second it is 10 etc.

print ((i+1)*2-n)
