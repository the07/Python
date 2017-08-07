number = 23
running = True

while running:

    guess = int(input('Enter a number'))

    if guess == number:
        print('Wow! That is correct')
        running = False

    elif guess < number:
        print('A little higher')

    else:
        print('A little lower')
