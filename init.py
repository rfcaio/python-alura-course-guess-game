
import guess
import hangman

print('\n***** (1) GUESS GAME')
print('***** (2) HANGMAN GAME')

game_option = int(input('\n***** CHOOSE YOUR GAME '))

if (game_option == 1):
    guess.init()
elif (game_option == 2):
    hangman.init()
else:
    print('\n***** INVALID OPTION!')
