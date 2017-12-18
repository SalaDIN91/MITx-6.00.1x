# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:33:52 2017

@author: Mayur
"""

# =============================================================================
# Problem 4
# 
# Write a Python function that creates and returns a list of prime numbers 
# between 2 and N, inclusive, sorted in increasing order. A prime number is a 
# number that is divisible only by 1 and itself. This function takes in an 
# integer and returns a list of integers.
# =============================================================================

#code
import math
def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''   
    primeList = []
    num = 2
    while num <= N:
        flag = False
        for prime in primeList[:int(math.sqrt(num))]:
            if num % prime == 0:
                flag = True
                break
        if not flag:
            primeList.append(num)
        num += 1
    return primeList