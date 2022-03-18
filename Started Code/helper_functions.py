import colorify

def update(score:str):
    '''str --> None
    Function to update the database file with new score'''
    
def list_scores():
    '''None --> List
    Returns a list of previous scores'''

def wins():
    '''None -> List
    Returns a list of number attempts, wins and losses'''
    

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

def getword():
    '''None -> Str
    Return a random word form words.txt'''

def isvalid(word:str,guessed_words:list):
    '''str, list -> str
    Return 
    'You must enter a valid 5-letter word!' if the word isn't five lettered
    'The word you entered is not valid!' if the word is not in valid_words.txt
    'You entered that word already!' if the word is already entered by the player'''
