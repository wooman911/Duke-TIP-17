#By Jungwoo Jang
from __future__ import print_function
import numpy
# print_Hangman's current state
def print_Hangman(number_Wrong):
    #Hangman "images" for each number of wrong guesses
    if number_Wrong == 0:
        print("   -------------")
        print("    I          I")
        print("    I          I")
        print("    I   ")
        print("    I   ")
        print("    I   ")
        print("    I   ")
        print("    I   ")
        print("    I   ")
        print("---------")
    else:
        pass
    if number_Wrong == 1:
        print("   -------------")
        print("    I          I")
        print("    I          I")
        print("    I          O")
        print("    I   ")
        print("    I   ")
        print("    I   ")
        print("    I   ")
        print("    I   ")
        print("---------")
    else:
        pass
    if number_Wrong == 2:
        print("   -------------")
        print("    I          I")
        print("    I          I")
        print("    I          O")
        print("    I          I")
        print("    I          I")
        print("    I           ")
        print("    I   ")
        print("    I   ")
        print("---------")
    else:
        pass
    if number_Wrong == 3:
        print("   -------------")
        print("    I          I")
        print("    I          I")
        print("    I          O")
        print("    I     -----I")
        print("    I          I")
        print("    I           ")
        print("    I           ")
        print("    I   ")
        print("---------")
    else:
        pass
    if number_Wrong == 4:
        print("   -------------")
        print("    I          I")
        print("    I          I")
        print("    I          O")
        print("    I     -----I-----")
        print("    I          I")
        print("    I   ")
        print("    I   ")
        print("    I   ")
        print("---------")
    else:
        pass
    if number_Wrong == 5:
        print("   -------------")
        print("    I          I")
        print("    I          I")
        print("    I          O")
        print("    I     -----I-----")
        print("    I          I")
        print("    I         /")
        print("    I        /")
        print("    I       /")
        print("---------")
    else:
        pass
    if number_Wrong == 6:
        print("   -------------")
        print("    I          I")
        print("    I          I")
        print("    I          O")
        print("    I     -----I-----")
        print("    I          I")
        print("    I         / I")
        print("    I        /  I")
        print("    I       /   I")
        print("---------")
        print("GAME OVER! HE DEAD")
    else:
        pass
def printBlanks(word, correctLetters):
    solved = True
    for l in word:
        if l in correctLetters:
            print(l+" ", end="")
        else:
            print("_ ", end = "")
            solved = False
    print()
    print()
    return solved
#The list of words
options = ["computer", "respect", "backpack", "programming"]
# The list that holds the correct letters
correctLetters = []
# The variable that counts all incorrect guesses (up to 6)
incorrectGuess = 0
# Picks a random word to be used
word = numpy.random.choice(options)
#Repeats
while True:
    #Printing the status of hangman
    print_Hangman(incorrectGuess)
    #Prints the word blanks and sees word was solved
    solved = printBlanks(word, correctLetters)
    # Telling Game Over of You Win to the player
    if incorrectGuess == 6:
        print("Game Over")
        break
    if solved:
        print("You win!")
        break
    # Define a variable to hold user input
    user_input=""
    # Loop until they give a letter
    while user_input == "":
        user_input = raw_input("Guess a Letter-->")
    #Telling the player that his or her choice was correct and adding that letter to the empty space
    if user_input in word:
        correctLetters.append(user_input)
        print("Correct!")
    #Adding plus 1 to the number of incorrect guesses and telling the player their guess was wrong.
    else:
        incorrectGuess += 1
        print("It's Wrong")
    print()
#Revealing the word to the player
print(word)
