import colorify, wordgen, time, sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)

def wordle():
    actual = wordgen.getword()
    guesses = 0
    print(actual)
    print('You only have 6 tries to guess a five letter word. Good Luck! \n\n')
    while guesses<6:
        guesses +=1
        guessed = input(f'Try {guesses}:  ')
        if len(guessed)!=5:
            guesses -=1
            print('You must guess a 5-letter word!')       
        elif guessed == actual:
            delay_print(colorify.colorit(guessed, actual)+f'\nYAAAAY YOU FOUND THE WORD. IT WAS {actual.upper()}'+ '\n')
            break
        #elif not wordgen.isvalid(guessed):
         #   guesses -=1
          #  print('The word you entered is not a valid word')
        else:
            delay_print(colorify.colorit(guessed,actual)+'\n')
    if guesses>=6 and guessed != actual:
        print('Better luck next time!')

wordle()
