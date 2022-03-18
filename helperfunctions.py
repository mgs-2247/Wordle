import re, colorify, random

def update(score:str):
    '''Function to update the database file with new score and '''
    data = open('database.txt', 'r').read()
    match = re.search('(\d+) \| ((\d )*)', data)
    prev_attempts, scores = match.group(1), match.group(2)
    newdata = f'{str(int(prev_attempts)+1)} | {scores}{score} '
    
    open('database.txt', 'w').write(newdata)
    
def list_scores():
    data = open('database.txt', 'r').read()
    match = re.search('(\d+) \| ((\d )*)', data)
    scores = match.group(2)
    return list(scores.replace(' ', ''))

def wins():
    data = open('database.txt', 'r').read()
    match = re.search('(\d+) \| ((\d )*)', data)
    attempts = int(match.group(1))
    score_list = list_scores()
    loses = score_list.count('0')
    wins = attempts - loses
    return [attempts, wins, loses]

def howtoplay():
    return f'''You have just one simple objective, to guess a five-letter word by entering characters. 
You are offered six attempts to get the word right. When you enter the alphabets, they are highlighted in 
different colors to indicate whether you have it right or not. For instance, if the alphabet entered is in
the word and in the correct spot, the character will turn green, and if wrong the character will turn yellow.
So what does it mean when you enter an alphabet and the character turns red? It means you have typed the 
wrong alphabet in the wrong spot.
For example, let's say the word to be guessed is 'SHARK', and you guess 'SAILS',
{colorify.colorit('sails', 'shark')} '''


def stats():
    return f'''Wins = {colorify.colored(wins()[1], 'green')}
Lost = {colorify.colored(wins()[2],'red')}
Win Percentage = {round(wins()[1]/wins()[0]*100,2)}%
    '''

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
