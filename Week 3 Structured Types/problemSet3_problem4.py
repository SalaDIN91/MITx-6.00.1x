# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 01:29:43 2017

@author: Mayur
"""
"""
Problem 4 - The Game

Now you will implement the function hangman, which takes one parameter - 
the secretWord the user is to guess. This starts up an interactive game of 
Hangman between the user and the computer. Be sure you take advantage of the 
three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions 
(at the top of ps3_hangman.py) to load the words and pick a random one. 
Note that the functions loadWords and chooseWord should only be used on 
your local machine, not in the tutor. When you enter in your solution in 
the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()

Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player 
guesses a letter, the guessed letter must be removed from availableLetters 
(and if they guess a letter that is not in availableLetters, you should print 
a message telling them they've already guessed that - so try again!).

"""
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    done = True
    for letter in secretWord:
        if letter in lettersGuessed:
            done = True
        else:
            return not done
    return done


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    disp = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            disp = disp + letter + ' '
        else:
            disp = disp + '_ '
    return disp


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lettersNotGuessed = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in lettersNotGuessed:
            lettersNotGuessed = lettersNotGuessed.replace(letter,'')
    return lettersNotGuessed
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")
    lettersGuessed = []
    guess = 8
    while guess > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print("You have", guess, "guesses left.")
        print("Available Letters:", getAvailableLetters(lettersGuessed));
        guessedLetter = input("Please guess a letter: ")
        if guessedLetter in lettersGuessed:
            print("Oops! You've already guessed that letter:", 
                  getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
        else:
            lettersGuessed.append(guessedLetter)
            if guessedLetter in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
                if isWordGuessed(secretWord, lettersGuessed):
                    return print("Congratulations, you won!")    
            else:
                print("Oops! That letter is not in my word:", 
                     getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
                guess -= 1
    return print("Sorry, you ran out of guesses. The word was " +secretWord +str('.'))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
