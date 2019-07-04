from random import randrange

def equals(guess, secret):
    return secret == guess


def get_quantity_of_turns(difficulty_level):
    if (difficulty_level == 1):
        return 20
    elif (difficulty_level == 2):
        return 10
    else:
        return 5


def is_greater_than(guess, secret):
    return guess > secret


def is_out_of_range(guess, start = 1, end = 100):
    return guess < start or guess > end


def show_status(turn, turns):
    return 'TURN {} OF {}'.format(turn, turns)


def update_points(points, guess, secret):
    return points - abs(guess - secret)


def init():
    points = 1000
    secret = randrange(1, 101)
    turns = 0
    print('\n***** WELCOME TO THE GUESS GAME\n')

    print('***** (1) EASY')
    print('***** (2) MEDIUM')
    print('***** (3) HARD')
    difficulty = int(input('\n***** CHOOSE YOUR DESTINY '))

    turns = get_quantity_of_turns(difficulty)

    for turn in range(1, turns + 1):
        print('\n***** {}\n'.format(show_status(turn, turns)))

        guess = int(input('ENTER A NUMBER BETWEEN 1 AND 100: '))

        if (is_out_of_range(guess)):
            print('\nNUMBER OUT OF RANGE!!!')
            continue

        if (equals(secret, guess)):
            print('\nYES! YOU HIT THE NUMBER.')
            print('\nYOU SCORED {} POINTS.'.format(points))
            break
        else:
            print('\nYOU DID NOT HIT THE SECRET NUMBER.')
            if (is_greater_than(guess, secret)):
                print('{} IS GREATER THAN SECRET NUMBER.'.format(guess))
            else:
                print('{} IS LOWER THAN SECRET NUMBER.'.format(guess))
            points = update_points(points, guess, secret)
    print('\n***** THE GAME IS OVER.\n')
