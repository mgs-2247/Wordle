import colorify, wordgen, time, sys, wordle

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)

def alpha():
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
            print('Some boring stats')
        elif command =='3':
            print('Help goes here')
        print('----------------------------------------------')
        if input('Press any key to open the main menu. Enter 0 to exit\n') == '0':
            command = False
           
alpha()
