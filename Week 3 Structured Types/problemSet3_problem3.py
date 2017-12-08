# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 01:22:43 2017

@author: Mayur
"""
"""
Problem 3 - Printing Out all Available Letters

Next, implement the function getAvailableLetters that takes in one parameter - 
a list of letters, lettersGuessed. This function returns a string that is 
comprised of lowercase English letters - all lowercase English letters that are 
not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz

Note that this function should return the letters in alphabetical order, 
as in the example above.

For this function, you may assume that all the letters in lettersGuessed 
are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string 
comprised of all lowercase letters:

>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
"""

#code
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