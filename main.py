
import time, sys, wordle, helperfunctions

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)

def main():
    command = True
    
    while command:
        command = input('''Welcome to Wordle!
    What would you like to do?
    0) Exit Game
    1) Play
    2) View stats
    3) How to play?\n''')
        if command == '0':
            command = False
        elif command == '1':
            wordle.wordle()
        elif command =='2':
            print(helperfunctions.stats())
        elif command =='3':
            print(helperfunctions.howtoplay())
        print('----------------------------------------------')
        if input('Press any key to continue.....\n') == '0':
            command = False
           
main()
