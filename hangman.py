
def has_hanged(errors):
    return errors >= 5


def has_won(score):
    return '_' not in score


def sanitize(word):
    return word.strip().lower()


def init():
    errors = 0
    secret = 'ermac'
    score = ['_' for word in secret]

    print('\n***** WELCOME TO THE HANGMAN GAME\n')

    print('***** SCORE: {}'.format(score))

    while (not has_hanged(errors) and not has_won(score)):
        print('***** {} ERROR{} LEFT'.format(5 - errors, 'S' if errors < 4 else ''))
        guess = sanitize(input('***** CHOOSE A LETTER '))

        if (guess in secret):
            index = 0
            for letter in secret:
                if (letter == guess):
                    score[index] = guess
                index += 1
        else:
            errors += 1
        print('\n***** SCORE: {}'.format(score))

    print('***** YOU WON THE GAME') if has_won(score) else print('***** YOU LOST THE GAME')

if (__name__ == '__main__'):
    init()
