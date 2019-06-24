
secret = 47

print('\n***** WELCOME TO THE GUESS GAME *****\n')

guess = input('ENTER A NUMBER: ')

if (int(guess) == secret):
    print('YES! YOU HIT THE NUMBER.')
else:
    print('YOU DID NOT HIT THE NUMBER.')
