from termcolor import colored

def colorit(guessed_word, word): #guessed word is the one guessed by the player and word is the correct word that is to be guessed
    gw = list(guessed_word)
    w = list(word)
    colors = []
    output = ''
    resolved = []
    for i in range(5):
        if gw[i] == w[i]:
            colors.append('green')
            resolved.append(i)
        elif gw[i] in w:
            colors.append('yellow')
            
        else:
            colors.append('red')
        output = output + colored(gw[i].upper(),colors[i]) + '   '
    return output