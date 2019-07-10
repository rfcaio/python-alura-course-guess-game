
def sanitize(word):
    return word.strip().lower()


def init():
    has_hanged = False
    has_won = False
    score = ['_', '_', '_', '_', '_', '_', '_', '_']
    secret = 'scorpion'

    print('\n***** WELCOME TO THE HANGMAN GAME\n')

    print('***** SCORE: {}'.format(score))

    while (not has_hanged and not has_won):
        guess = sanitize(input('***** CHOOSE A LETTER '))
        index = 0
        for letter in secret:
            if (letter == guess):
                score[index] = guess
            index += 1
        print('\n***** SCORE: {}'.format(score))


if (__name__ == '__main__'):
    init()
