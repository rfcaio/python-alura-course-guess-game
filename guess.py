
def equals(guess, secret):
    return secret == guess


def is_greater_than(guess, secret):
    return guess > secret


def show_status(turn, turns):
    return 'TURN {} OF {}'.format(turn, turns)


def init():
    secret = 47
    turn = 1
    turns = 3
    print('\n***** WELCOME TO THE GUESS GAME *****\n')

    while (turn <= turns):
        print('\n***** {} ******\n'.format(show_status(turn, turns)))

        guess = input('ENTER A NUMBER: ')

        if (equals(secret, int(guess))):
            print('\nYES! YOU HIT THE NUMBER.')
            break
        else:
            turn += 1
            print('\nYOU DID NOT HIT THE SECRET NUMBER.')
            if (is_greater_than(int(guess), secret)):
                print('{} IS GREATER THAN SECRET NUMBER.'.format(guess))
            else:
                print('{} IS LOWER THAN SECRET NUMBER.'.format(guess))
    print('\n***** THE GAME IS OVER. *****\n')
