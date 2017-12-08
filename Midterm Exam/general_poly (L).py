# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:05:26 2017

@author: Mayur
"""
"""
Exercise 7:
    
L, a list of numbers (n0, n1, n2, ... nk) 
Returns a function, which when applied to a value x, returns the value 
n0 * x^k + n1 * x^(k-1) + ... nk * x^0 

If L = [1, 2, 3, 4]

Invoking function with list L and value of x = 10 -

general_poly(L)(10)

result should be 1234
i.e. 1 * 10^3 + 2 * 10^2 + 3 * 10^1 + 4 * 10^0

"""

#code
def general_poly (L):
    """ 
    L: a list of numbers (n0, n1, n2, ... nk)
    Returns: a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """    
    def func(x):
        value = 0
        k = len(L) - 1
        for num in L:
            value = value + num * (x ** k)
            k -= 1
        return value
    return func
