import random

wordfile = open('words.txt', 'r')
wordlist = wordfile.readlines()

validwordfile = open('valid-words', 'r')
validwordlist = validwordfile.readlines()

def getword():
    return random.choice(wordlist).rstrip('\n')

def isvalid(word:str):
    return word+'\n' in validwordlist
