from distutils.util import change_root
import colorify
import wordgen

def wordle():
    actual = wordgen.getword()
    guesses = 0
    print('You only have 6 tries to guess a five letter word. Good Luck! \n\n')
    print(actual)
    while guesses<6:
        guesses +=1
        guessed = input(f'Try {guesses}:  ')
        if len(guessed)!=5:
            guesses -=1
            print('You must guess a 5-letter word!')
        elif not wordgen.isvalid(guessed):
            guesses -= 1
            print('The word you entered is not valid!')        
        elif guessed == actual:
            print(colorify.colorit(guessed, actual)+f'\nYAAAAY YOU FOUND THE WORD. IT WAS {actual.upper()}')
            break
        else:
            print(colorify.colorit(guessed,actual))
    if guesses>=6 and guessed != actual:
        print('Better luck next time!')

wordle()
