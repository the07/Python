import random

# safely make an int
#limit guesses
#too high or low message
#play again

def game():

    #generate a random number between 1 and 10
    secret_number = random.randint(1,10)
    guesses = []
    while len(guesses) < 5:
        try:
            #get a number guess from the player
            guess = int(input('Enter a number between 1 and 10'))
        except ValueError:
            print('{} is not a number'.format(guess))
        else:
            #compare guess to a secret number
            if guess == secret_number:
                print('Yay, you got my number')
                break
            elif guess < secret_number:
                print ('My number is higher than that')
            else:
                print('My number is less than that')
            guesses.append(guess)
    else:
        print('You did not get it. My number was {}'.format(secret_number))
    play_again = input('Do you want to play again? Y/N')
    if play_again.lower() != 'n':
        game()
    else:
        print('BYE!')
game()
