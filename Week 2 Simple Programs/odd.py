# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:31:06 2017

@author: Mayur
"""
"""
Exercise: odd

Write a Python function, odd, that takes in one number and returns True when 
the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.
"""

#code
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return not x % 2 == 0
