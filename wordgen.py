import random

wordfile = open('words.txt', 'r')
wordlist = wordfile.readlines()

validwordfile = open('valid-words', 'r')
validwordlist = validwordfile.readlines()

def getword():
    return random.choice(wordlist).rstrip('\n')

def isvalid(word:str,guessed_words:list):
    if len(word)!=5:
        return 'You must enter a valid 5-letter word!'
    elif word+'\n' not in validwordlist:
        return 'The word you entered is not valid!'
    elif word in guessed_words:
        return 'You entered that word already!'
    else: return 'valid'
