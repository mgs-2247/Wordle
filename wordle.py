import colorify, wordgen, time, sys, storage

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def wordle():
    actual = wordgen.getword()
    guesses = 0
    guessed_words = []
    print(actual)
    print('You only have 6 tries to guess a five letter word. You can quit the game at any time by entering 0.\n Good Luck! \n\n')
    while guesses<6:
        guesses +=1
        guessed = input(f'Try {guesses}:  ')
        if guessed == '0':
            print('Exitting.....')
            time.sleep(1)
            print('Exitted. Thanks for playing!')
            break
        elif wordgen.isvalid(guessed,guessed_words)!='valid':
            guesses -=1
            print(wordgen.isvalid(guessed,guessed_words))       
        elif guessed == actual:
            delay_print(colorify.colorit(guessed, actual)+'\n')
            print(f'\nYAAAAY YOU FOUND THE WORD. IT WAS {actual.upper()}'+'\n')
            break
        else:
            guessed_words.append(guessed)
            delay_print(colorify.colorit(guessed,actual)+'\n')
    
    if guesses>=6 and guessed != actual:
        storage.update('0')
        print('Better luck next time!')
    else:storage.update(str(guesses))

