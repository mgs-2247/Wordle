IFS wordle starter code
colorify.py - Contains already defined function which colors the word according to the coloring scheme.
database.txt - File used to store previous scores of the user
helper_functions.py - Contains function headers some helper functions used in various places in the project
                    update() - Function to update the database file with new score
                    list_scores() - Function to return a list of previous scores stored in database.txt
                    wins() - Function to return a three-membered list with number of attempts, wins. loses as the elemnts.
                    howtoplay() - A defined function which contains a docstring on how to play the game
                    stats() A defined function to return the stats(wins, loses and win percentage). Uses wins() function
                    getword() - Function to return a random word from words.txt
                    isvalid() - Function to return 
                    'You must enter a valid 5-letter word!' if the word isn't five lettered
                    'The word you entered is not valid!' if the word is not in valid_words.txt
                    'You entered that word already!' if the word is already entered by the player
                    else return 'valid' 

main.py - Contains a defined function, delayed_print() which helps in printing the output letter by letter. Nothing functional, completely decoratory.
          Contains function header for main(). You must create a menu similar to the one showed in the demo. 
valid_words.txt - Contains a list of valid words. You must use this in your isvalid() function
wordle.py - Contains the complete driver code for the game. It uses helper functions like getword(), isvalid(), colorit(), update()

Your goal is to define the incomplete functions in helper_functions.py and main.py.
