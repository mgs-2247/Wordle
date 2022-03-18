from termcolor import colored

def colorit(guessed_word, word): #guessed word is the one guessed by the player and word is the correct word that is to be guessed
    gw = list(guessed_word)
    w = list(word)
    colors = []
    output = ''
    for index in range(5):
        if gw[index] == w[index]:
            colors.append('green')
        elif gw[index] in w:
            colors.append('yellow')          
        else:
            colors.append('red')
        output = output + colored(gw[index].upper(),colors[index]) + '   '
    return output