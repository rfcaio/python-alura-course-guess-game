from random import randrange

def get_fighters_from_file(file_name):
    fighters = []
    fighters_file = open(file_name, 'r')
    for fighter in fighters_file:
        fighters.append(sanitize(fighter))
    fighters_file.close()
    return fighters


def get_random_fighter(fighters):
    return fighters[randrange(0, len(fighters))]


def has_hanged(errors):
    return errors >= 5


def has_won(score):
    return '_' not in score


def sanitize(word):
    return word.strip().lower()


def update_score(score, secret, guess):
    if (guess in secret):
        index = 0
        for letter in secret:
            if (letter == guess):
                score[index] = guess
            index += 1
    return score


def init():
    errors = 0
    secret = get_random_fighter(get_fighters_from_file('fighters.txt'))
    score = ['_' for word in secret]

    print('\n***** WELCOME TO THE HANGMAN GAME\n')

    print('***** SCORE: {}'.format(score))

    while (not has_hanged(errors) and not has_won(score)):
        print('***** {} ERROR{} LEFT'.format(5 - errors, 'S' if errors < 4 else ''))
        guess = sanitize(input('***** CHOOSE A LETTER '))

        if (guess in secret):
            score = update_score(score, secret, guess)
        else:
            errors += 1
        print('\n***** SCORE: {}'.format(score))

    print('***** YOU WON THE GAME') if has_won(score) else print('***** YOU LOST THE GAME')

if (__name__ == '__main__'):
    init()
