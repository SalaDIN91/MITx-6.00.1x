# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:43:22 2017

@author: Mayur
"""
"""
Exercise: gcd recur

The greatest common divisor of two positive integers is the largest integer that 
divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common 
divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. This 
function takes in two positive integers and returns one integer.
"""

#code
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0 or b == 0:
     return max(a,b)
    else:
     return gcdRecur(min(a,b), max(a,b)%min(a,b))
