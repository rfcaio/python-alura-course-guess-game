
def equals(guess, secret):
    return secret == guess


def is_greater_than(guess, secret):
    return guess > secret


def init():
    secret = 47

    print('\n***** WELCOME TO THE GUESS GAME *****\n')

    guess = input('ENTER A NUMBER: ')

    if (equals(secret, int(guess))):
        print('\nYES! YOU HIT THE NUMBER.\n')
    else:
        print('\nYOU DID NOT HIT THE SECRET NUMBER.')
        if (is_greater_than(int(guess), secret)):
            print('{} IS GREATER THAN SECRET NUMBER.'.format(guess))
        else:
            print('{} IS LOWER THAN SECRET NUMBER.'.format(guess))
