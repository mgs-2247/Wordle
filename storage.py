import re


def update(score:str):
    data = open('database.txt', 'r').read()
    match = re.search('(\d+) \| ((\d )+)', data)
    prev_attempts, scores = match.group(1), match.group(2)
    newdata = f'{str(int(prev_attempts)+1)} | {scores}{score} '
    
    open('database.txt', 'w').write(newdata)
    
    
def list_scores():
    data = open('database.txt', 'r').read()
    match = re.search('(\d+) \| ((\d )+)', data)
    scores = match.group(2)
    return list(scores.replace(' ', ''))
update('1')



