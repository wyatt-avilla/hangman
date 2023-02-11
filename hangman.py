# author: Wyatt Avilla
# date: 10/3/2022
# file: hangman.py is a program that opens a word bank, asks the user to chose game settings, and then runs a game of hangman
# input: dictionary file (in same directory) and desired game settings
# output: hangman game

from random import choice, randint, random

def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    for i in range(max_size+1):
        dictionary.update({i:[]})
    try:
        with open (filename, "r") as txt:
            for x in txt:
                word = x.strip()
                if word.count("-") == 1:
                    if len(word) <  13:
                        dictionary[len(word)].append(word.lower())
                else:
                    if word.isalpha():
                        if len(word) < 13:
                            dictionary[len(word)].append(word.lower())
            txt.close()
            return(dictionary)
                
    except Exception :
        print("Error in opening file")

def get_game_options() :
    size = input("Please choose a size of a word to be guessed [3 – 12, default any size]:\n")
    if size.isnumeric() and 3<=int(size)<=12:
        if len(dictionary.get(int(size))) > 0:
            print(f"The word size is set to {size}.")
            size = int(size)
        else:
            print("A dictionary word of any size will be chosen.")
            size = get_nonempty_key()
    else:
        print("A dictionary word of any size will be chosen.")
        size = get_nonempty_key()
    lives = input("Please choose a number of lives [1 – 10, default 5]:\n")
    if lives.isnumeric() and 1<=int(lives)<=10:
        print(f"You have {lives} lives.")
        lives = int(lives)
    else:
        lives = 5
        print(f"You have {lives} lives.")

    return (size, lives)

def get_nonempty_key():
    done = False
    while done == False:
        x = randint(3, 12)
        if len(dictionary.get(x)) > 0:
            return x
        else:
            continue


dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located
dictionary = import_dictionary(dictionary_file)


print("Welcome to Hangman!")  # main loop
while True: 
    chosenletters = []                  # letters picked by the user during the game
    userchoices = get_game_options()
    wordsize = userchoices[0]
    userlives = userchoices[1]
    censored = []                       # randomly selected word with letters replaced by "__"
    words = (dictionary[wordsize])      # list of words with chosen length
    guessword = words[(randint(0,(len(words)-1)))]  # word to be guessed by user
    livesdisplay = ["O"]*userlives
    for char in guessword:
        if char.isalpha():
            censored.append("__")
        else:
            censored.append(char)    
    while True:
        print("Letters chosen: " + ", ".join(chosenletters))
        print("  ".join(censored)+"   lives: "+str(userlives)+" "+"".join(livesdisplay))
        letterchoice = input("Please choose a new letter >\n").lower()
        try:
            if letterchoice.isalpha() and len(letterchoice) == 1:
                if letterchoice.upper() in chosenletters:
                    print("You have already chosen this letter.")
                elif letterchoice in guessword:
                    chosenletters.append(letterchoice.upper())
                    print("You guessed right!")
                    for i in range(len(guessword)):
                        if guessword[i] == letterchoice:
                            censored[i] = letterchoice.upper()
                elif letterchoice not in guessword:
                    chosenletters.append(letterchoice.upper())
                    print("You guessed wrong, you lost one life.")
                    userlives = userlives-1
                    n = livesdisplay.index("O")
                    livesdisplay[n] = "X"

        except:
            print("Invalid choice")
        if int(userlives) == 0:
            print("Letters chosen: " + ", ".join(chosenletters))
            print("  ".join(censored)+"   lives: "+str(userlives)+" "+"".join(livesdisplay))
            print(f"You lost! The word is {str(guessword).upper()}!")
            userchoice = input("Would you like to play again [Y/N]?\n").upper()
            if userchoice == "Y":
                break
            elif userchoice == "N":
                print("Goodbye!")
                exit()
            else:
                print("Goodbye!")
                exit()
        if "__" not in censored:
            print("You guessed right!")
            print("Letters chosen: " + ", ".join(chosenletters))
            print("  ".join(censored)+"   lives: "+str(userlives)+" "+"".join(livesdisplay))
            print(f"Congratulations!!! You Won! The word is {str(guessword).upper()}!")
            userchoice2 = input("Would you like to play again [Y/N]?\n").upper()
            if userchoice2 == "Y":
                break
            elif userchoice2 == "N":
                print("Goodbye!")
                exit()
            else:
                print("Goodbye!")
                exit()