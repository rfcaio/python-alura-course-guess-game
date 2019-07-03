from random import randrange

def equals(guess, secret):
    return secret == guess


def is_greater_than(guess, secret):
    return guess > secret


def is_out_of_range(guess, start = 1, end = 100):
    return guess < start or guess > end


def show_status(turn, turns):
    return 'TURN {} OF {}'.format(turn, turns)


def init():
    secret = randrange(1, 101)
    turns = 3
    print('\n***** WELCOME TO THE GUESS GAME\n')

    for turn in range(1, turns + 1):
        print('\n***** {}\n'.format(show_status(turn, turns)))

        guess = input('ENTER A NUMBER BETWEEN 1 AND 100: ')

        if (is_out_of_range(int(guess))):
            print('\nNUMBER OUT OF RANGE!!!')
            continue

        if (equals(secret, int(guess))):
            print('\nYES! YOU HIT THE NUMBER.')
            break
        else:
            print('\nYOU DID NOT HIT THE SECRET NUMBER.')
            if (is_greater_than(int(guess), secret)):
                print('{} IS GREATER THAN SECRET NUMBER.'.format(guess))
            else:
                print('{} IS LOWER THAN SECRET NUMBER.'.format(guess))
    print('\n***** THE GAME IS OVER.\n')
