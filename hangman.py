
def sanitize(word):
    return word.strip().lower()


def init():
    has_hanged = False
    has_won = False
    secret = 'scorpion'

    print('\n***** WELCOME TO THE HANGMAN GAME\n')

    while (not has_hanged and not has_won):
        guess = sanitize(input('***** CHOOSE A LETTER '))
        index = 0
        for letter in secret:
            if (letter == guess):
                print('***** FOUND {} IN INDEX {}'.format(letter, index))
            index += 1


if (__name__ == '__main__'):
    init()
