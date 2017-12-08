# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:38:04 2017

@author: Mayur
"""
"""
Exercise: power recur

Write a function recurPower(base, exp) which computes base^exp by recursively 
calling itself to solve a smaller version of the same problem, and then 
multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥0. It should return one numerical value. Your code 
must be recursive - use of the ** operator or looping constructs is not allowed.
"""

#code
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
      return 1
    else:
      return base*recurPower(base,exp-1)