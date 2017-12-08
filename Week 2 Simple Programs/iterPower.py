# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:32:41 2017

@author: Mayur
"""
"""
Exercise: power iter

Write an iterative function iterPower(base, exp) that calculates the exponential 
base^exp by simply using successive multiplication. For example, iterPower(base, exp) 
should compute base^exp by multiplying base times itself exp times. 
Write such a function below.

This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥ 0. It should return one numerical value. 
Your code must be iterative - use of the ** operator is not allowed.
"""

#code
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    power = 1
    while exp > 0:
      power = power*base
      exp -= 1
    return power