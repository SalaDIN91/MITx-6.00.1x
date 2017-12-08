# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:47:31 2017

@author: Mayur
"""
"""
Exercise 3:

Write a recursive Python function, given a non-negative integer N,
to calculate the no. of occurrences of digit 7 in N.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer.
"""

#code
def count7(N):
    '''
    N: a non-negative integer
    returns: no. of occurrences of digit 7 in the number N
    '''
    if N == 0:
        return 0
    elif N % 10 == 7:
        return 1 + count7(N // 10)
    else:
        return 0 + count7(N // 10)